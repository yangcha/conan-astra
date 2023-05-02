from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.errors import ConanInvalidConfiguration
from conan.tools.files import apply_conandata_patches, collect_libs, copy, export_conandata_patches, get, rmdir
from conan.tools.microsoft import is_msvc, is_msvc_static_runtime
import os

required_conan_version = ">=1.53.0"

class AstraRecipe(ConanFile):
    name = "astra-toolbox"
    version = "2.1.0"
    description = """The ASTRA Toolbox is a toolbox of high-performance GPU primitives for 2D and 3D tomography"""
    package_type = "library"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": True,
        "fPIC": True,
    }
    
    def export_sources(self):
        copy(self, "CMakeLists.txt", self.recipe_folder, os.path.join(self.export_sources_folder, 'src'))
    
    def validate(self):
        if self.info.settings.os == "Macos" and self.info.settings.arch == "armv8":
            raise ConanInvalidConfiguration("ARM v8 not supported")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        self.settings.rm_safe("compiler.cppstd")
        self.settings.rm_safe("compiler.libcxx")

    def layout(self):
        cmake_layout(self, src_folder="src")

    def requirements(self):
        self.requires("boost/1.78.0")
              
    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)
    
    def generate(self):
       tc = CMakeToolchain(self)
       tc.generate()

    def build(self):
       #apply_conandata_patches(self)
       cmake = CMake(self)
       cmake.configure()
       cmake.build()
       
    def package(self):
        copy(self, "COPYING", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        cmake = CMake(self)
        cmake.install()