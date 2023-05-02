cmake_minimum_required(VERSION 3.15)

set(PROJECT_NAME AstraCuda)

project(${PROJECT_NAME} LANGUAGES CUDA CXX)

enable_language(CUDA)
include(CheckLanguage)
check_language(CUDA)
find_package(CUDAToolkit)

set(CMAKE_CXX_STANDARD 17)
#include(${CMAKE_BINARY_DIR}/conanbuildinfo_multi.cmake)
#conan_basic_setup(TARGETS)

################################################################################
# Source groups
################################################################################
set(Algorithms__headers
    "include/astra/Algorithm.h"
    "include/astra/AlgorithmTypelist.h"
    "include/astra/ArtAlgorithm.h"
    "include/astra/AsyncAlgorithm.h"
    "include/astra/BackProjectionAlgorithm.h"
    "include/astra/CglsAlgorithm.h"
    "include/astra/CudaBackProjectionAlgorithm.h"
    "include/astra/CudaBackProjectionAlgorithm3D.h"
    "include/astra/FilteredBackProjectionAlgorithm.h"
    "include/astra/ForwardProjectionAlgorithm.h"
    "include/astra/PluginAlgorithmFactory.h"
    "include/astra/ReconstructionAlgorithm2D.h"
    "include/astra/ReconstructionAlgorithm3D.h"
    "include/astra/SartAlgorithm.h"
    "include/astra/SirtAlgorithm.h"
)
source_group("Algorithms\\headers" FILES ${Algorithms__headers})

set(Algorithms__source
    "src/Algorithm.cpp"
    "src/ArtAlgorithm.cpp"
    "src/AsyncAlgorithm.cpp"
    "src/BackProjectionAlgorithm.cpp"
    "src/CglsAlgorithm.cpp"
    "src/FilteredBackProjectionAlgorithm.cpp"
    "src/ForwardProjectionAlgorithm.cpp"
    "src/PluginAlgorithmFactory.cpp"
    "src/ReconstructionAlgorithm2D.cpp"
    "src/ReconstructionAlgorithm3D.cpp"
    "src/SartAlgorithm.cpp"
    "src/SirtAlgorithm.cpp"
)
source_group("Algorithms\\source" FILES ${Algorithms__source})

set(CUDA__astra_headers
    "include/astra/CudaCglsAlgorithm.h"
    "include/astra/CudaCglsAlgorithm3D.h"
    "include/astra/CudaDartMaskAlgorithm.h"
    "include/astra/CudaDartMaskAlgorithm3D.h"
    "include/astra/CudaDartSmoothingAlgorithm.h"
    "include/astra/CudaDartSmoothingAlgorithm3D.h"
    "include/astra/CudaDataOperationAlgorithm.h"
    "include/astra/CudaEMAlgorithm.h"
    "include/astra/CudaFDKAlgorithm3D.h"
    "include/astra/CudaFilteredBackProjectionAlgorithm.h"
    "include/astra/CudaForwardProjectionAlgorithm.h"
    "include/astra/CudaForwardProjectionAlgorithm3D.h"
    "include/astra/CudaProjector2D.h"
    "include/astra/CudaProjector3D.h"
    "include/astra/CudaReconstructionAlgorithm2D.h"
    "include/astra/CudaRoiSelectAlgorithm.h"
    "include/astra/CudaSartAlgorithm.h"
    "include/astra/CudaSirtAlgorithm.h"
    "include/astra/CudaSirtAlgorithm3D.h"
    "include/astra/Float32Data3DGPU.h"
    "include/astra/Float32ProjectionData3DGPU.h"
    "include/astra/Float32VolumeData3DGPU.h"
)
source_group("CUDA\\astra headers" FILES ${CUDA__astra_headers})

set(CUDA__astra_source
    "src/CudaBackProjectionAlgorithm.cpp"
    "src/CudaBackProjectionAlgorithm3D.cpp"
    "src/CudaCglsAlgorithm.cpp"
    "src/CudaCglsAlgorithm3D.cpp"
    "src/CudaDartMaskAlgorithm.cpp"
    "src/CudaDartMaskAlgorithm3D.cpp"
    "src/CudaDartSmoothingAlgorithm.cpp"
    "src/CudaDartSmoothingAlgorithm3D.cpp"
    "src/CudaDataOperationAlgorithm.cpp"
    "src/CudaEMAlgorithm.cpp"
    "src/CudaFDKAlgorithm3D.cpp"
    "src/CudaFilteredBackProjectionAlgorithm.cpp"
    "src/CudaForwardProjectionAlgorithm.cpp"
    "src/CudaForwardProjectionAlgorithm3D.cpp"
    "src/CudaProjector2D.cpp"
    "src/CudaProjector3D.cpp"
    "src/CudaReconstructionAlgorithm2D.cpp"
    "src/CudaRoiSelectAlgorithm.cpp"
    "src/CudaSartAlgorithm.cpp"
    "src/CudaSirtAlgorithm.cpp"
    "src/CudaSirtAlgorithm3D.cpp"
    "src/Float32Data3DGPU.cpp"
    "src/Float32ProjectionData3DGPU.cpp"
    "src/Float32VolumeData3DGPU.cpp"
)
source_group("CUDA\\astra source" FILES ${CUDA__astra_source})

set(CUDA__cuda_headers
    "include/astra/cuda/2d/algo.h"
    "include/astra/cuda/2d/arith.h"
    "include/astra/cuda/2d/astra.h"
    "include/astra/cuda/2d/cgls.h"
    "include/astra/cuda/2d/darthelper.h"
    "include/astra/cuda/2d/dims.h"
    "include/astra/cuda/2d/em.h"
    "include/astra/cuda/2d/fan_bp.h"
    "include/astra/cuda/2d/fan_fp.h"
    "include/astra/cuda/2d/fbp.h"
    "include/astra/cuda/2d/fft.h"
    "include/astra/cuda/2d/par_bp.h"
    "include/astra/cuda/2d/par_fp.h"
    "include/astra/cuda/2d/sart.h"
    "include/astra/cuda/2d/sirt.h"
    "include/astra/cuda/2d/util.h"
    "include/astra/cuda/3d/algo3d.h"
    "include/astra/cuda/3d/arith3d.h"
    "include/astra/cuda/3d/astra3d.h"
    "include/astra/cuda/3d/cgls3d.h"
    "include/astra/cuda/3d/cone_bp.h"
    "include/astra/cuda/3d/cone_fp.h"
    "include/astra/cuda/3d/darthelper3d.h"
    "include/astra/cuda/3d/dims3d.h"
    "include/astra/cuda/3d/fdk.h"
    "include/astra/cuda/3d/mem3d.h"
    "include/astra/cuda/3d/par3d_bp.h"
    "include/astra/cuda/3d/par3d_fp.h"
    "include/astra/cuda/3d/sirt3d.h"
    "include/astra/cuda/3d/util3d.h"
)
source_group("CUDA\\cuda headers" FILES ${CUDA__cuda_headers})

set(CUDA__cuda_source
    "cuda/2d/algo.cu"
    "cuda/2d/arith.cu"
    "cuda/2d/astra.cu"
    "cuda/2d/cgls.cu"
    "cuda/2d/darthelper.cu"
    "cuda/2d/em.cu"
    "cuda/2d/fan_bp.cu"
    "cuda/2d/fan_fp.cu"
    "cuda/2d/fbp.cu"
    "cuda/2d/fft.cu"
    "cuda/2d/par_bp.cu"
    "cuda/2d/par_fp.cu"
    "cuda/2d/sart.cu"
    "cuda/2d/sirt.cu"
    "cuda/2d/util.cu"
    "cuda/3d/algo3d.cu"
    "cuda/3d/arith3d.cu"
    "cuda/3d/astra3d.cu"
    "cuda/3d/cgls3d.cu"
    "cuda/3d/cone_bp.cu"
    "cuda/3d/cone_fp.cu"
    "cuda/3d/darthelper3d.cu"
    "cuda/3d/fdk.cu"
    "cuda/3d/mem3d.cu"
    "cuda/3d/par3d_bp.cu"
    "cuda/3d/par3d_fp.cu"
    "cuda/3d/sirt3d.cu"
    "cuda/3d/util3d.cu"
)
source_group("CUDA\\cuda source" FILES ${CUDA__cuda_source})

set(Data_Structures__headers
    "include/astra/Float32Data.h"
    "include/astra/Float32Data2D.h"
    "include/astra/Float32Data3D.h"
    "include/astra/Float32Data3DMemory.h"
    "include/astra/Float32ProjectionData2D.h"
    "include/astra/Float32ProjectionData3D.h"
    "include/astra/Float32ProjectionData3DMemory.h"
    "include/astra/Float32VolumeData2D.h"
    "include/astra/Float32VolumeData3D.h"
    "include/astra/Float32VolumeData3DMemory.h"
    "include/astra/SparseMatrix.h"
)
source_group("Data Structures\\headers" FILES ${Data_Structures__headers})

set(Data_Structures__source
    "src/Float32Data.cpp"
    "src/Float32Data2D.cpp"
    "src/Float32Data3D.cpp"
    "src/Float32Data3DMemory.cpp"
    "src/Float32ProjectionData2D.cpp"
    "src/Float32ProjectionData3D.cpp"
    "src/Float32ProjectionData3DMemory.cpp"
    "src/Float32VolumeData2D.cpp"
    "src/Float32VolumeData3D.cpp"
    "src/Float32VolumeData3DMemory.cpp"
    "src/SparseMatrix.cpp"
)
source_group("Data Structures\\source" FILES ${Data_Structures__source})

set(Geometries__headers
    "include/astra/ConeProjectionGeometry3D.h"
    "include/astra/ConeVecProjectionGeometry3D.h"
    "include/astra/FanFlatProjectionGeometry2D.h"
    "include/astra/FanFlatVecProjectionGeometry2D.h"
    "include/astra/GeometryUtil2D.h"
    "include/astra/GeometryUtil3D.h"
    "include/astra/ParallelProjectionGeometry2D.h"
    "include/astra/ParallelProjectionGeometry3D.h"
    "include/astra/ParallelVecProjectionGeometry2D.h"
    "include/astra/ParallelVecProjectionGeometry3D.h"
    "include/astra/ProjectionGeometry2D.h"
    "include/astra/ProjectionGeometry3D.h"
    "include/astra/SparseMatrixProjectionGeometry2D.h"
    "include/astra/VolumeGeometry2D.h"
    "include/astra/VolumeGeometry3D.h"
)
source_group("Geometries\\headers" FILES ${Geometries__headers})

set(Geometries__source
    "src/ConeProjectionGeometry3D.cpp"
    "src/ConeVecProjectionGeometry3D.cpp"
    "src/FanFlatProjectionGeometry2D.cpp"
    "src/FanFlatVecProjectionGeometry2D.cpp"
    "src/GeometryUtil2D.cpp"
    "src/GeometryUtil3D.cpp"
    "src/ParallelProjectionGeometry2D.cpp"
    "src/ParallelProjectionGeometry3D.cpp"
    "src/ParallelVecProjectionGeometry2D.cpp"
    "src/ParallelVecProjectionGeometry3D.cpp"
    "src/ProjectionGeometry2D.cpp"
    "src/ProjectionGeometry3D.cpp"
    "src/SparseMatrixProjectionGeometry2D.cpp"
    "src/VolumeGeometry2D.cpp"
    "src/VolumeGeometry3D.cpp"
)
source_group("Geometries\\source" FILES ${Geometries__source})

set(Global__Other__headers
    "include/astra/AstraObjectFactory.h"
    "include/astra/AstraObjectManager.h"
    "include/astra/clog.h"
    "include/astra/CompositeGeometryManager.h"
    "include/astra/Config.h"
    "include/astra/Features.h"
    "include/astra/Filters.h"
    "include/astra/Fourier.h"
    "include/astra/Globals.h"
    "include/astra/Logging.h"
    "include/astra/PlatformDepSystemCode.h"
    "include/astra/Singleton.h"
    "include/astra/TypeList.h"
    "include/astra/Utilities.h"
    "include/astra/Vector3D.h"
    "include/astra/XMLDocument.h"
    "include/astra/XMLNode.h"
)
source_group("Global & Other\\headers" FILES ${Global__Other__headers})

set(Global__Other__source
    "src/AstraObjectFactory.cpp"
    "src/AstraObjectManager.cpp"
    "src/CompositeGeometryManager.cpp"
    "src/Config.cpp"
    "src/Features.cpp"
    "src/Filters.cpp"
    "src/Fourier.cpp"
    "src/Globals.cpp"
    "src/Logging.cpp"
    "src/PlatformDepSystemCode.cpp"
    "src/Utilities.cpp"
    "src/XMLDocument.cpp"
    "src/XMLNode.cpp"
)
source_group("Global & Other\\source" FILES ${Global__Other__source})

set(Projectors__headers
    "include/astra/DataProjector.h"
    "include/astra/DataProjectorPolicies.h"
    "include/astra/FanFlatBeamLineKernelProjector2D.h"
    "include/astra/FanFlatBeamStripKernelProjector2D.h"
    "include/astra/ParallelBeamBlobKernelProjector2D.h"
    "include/astra/ParallelBeamDistanceDrivenProjector2D.h"
    "include/astra/ParallelBeamLinearKernelProjector2D.h"
    "include/astra/ParallelBeamLineKernelProjector2D.h"
    "include/astra/ParallelBeamStripKernelProjector2D.h"
    "include/astra/Projector2D.h"
    "include/astra/Projector3D.h"
    "include/astra/ProjectorTypelist.h"
    "include/astra/SparseMatrixProjector2D.h"
)
source_group("Projectors\\headers" FILES ${Projectors__headers})

set(Projectors__inline
    "include/astra/DataProjectorPolicies.inl"
    "include/astra/FanFlatBeamLineKernelProjector2D.inl"
    "include/astra/FanFlatBeamStripKernelProjector2D.inl"
    "include/astra/ParallelBeamBlobKernelProjector2D.inl"
    "include/astra/ParallelBeamDistanceDrivenProjector2D.inl"
    "include/astra/ParallelBeamLinearKernelProjector2D.inl"
    "include/astra/ParallelBeamLineKernelProjector2D.inl"
    "include/astra/ParallelBeamStripKernelProjector2D.inl"
    "include/astra/SparseMatrixProjector2D.inl"
)
source_group("Projectors\\inline" FILES ${Projectors__inline})

set(Projectors__source
    "src/DataProjector.cpp"
    "src/DataProjectorPolicies.cpp"
    "src/FanFlatBeamLineKernelProjector2D.cpp"
    "src/FanFlatBeamStripKernelProjector2D.cpp"
    "src/ParallelBeamBlobKernelProjector2D.cpp"
    "src/ParallelBeamDistanceDrivenProjector2D.cpp"
    "src/ParallelBeamLinearKernelProjector2D.cpp"
    "src/ParallelBeamLineKernelProjector2D.cpp"
    "src/ParallelBeamStripKernelProjector2D.cpp"
    "src/Projector2D.cpp"
    "src/Projector3D.cpp"
    "src/SparseMatrixProjector2D.cpp"
)
source_group("Projectors\\source" FILES ${Projectors__source})

set(ALL_FILES
    ${Algorithms__headers}
    ${Algorithms__source}
    ${CUDA__astra_headers}
    ${CUDA__astra_source}
    ${CUDA__cuda_headers}
    ${CUDA__cuda_source}
    ${Data_Structures__headers}
    ${Data_Structures__source}
    ${Geometries__headers}
    ${Geometries__source}
    ${Global__Other__headers}
    ${Global__Other__source}
    ${Projectors__headers}
    ${Projectors__inline}
    ${Projectors__source}
)

################################################################################
# Targets
################################################################################
set(PROJECT_ASTRA AstraCuda64)
add_library(${PROJECT_ASTRA} SHARED ${ALL_FILES})

set(Boost_USE_STATIC_LIBS        ON)  # only find static libs
set(Boost_USE_DEBUG_LIBS        OFF)  # ignore debug libs and
set(Boost_USE_RELEASE_LIBS       ON)  # only find release libs
set(Boost_USE_MULTITHREADED      ON)
set(Boost_USE_STATIC_RUNTIME    OFF)
find_package(Boost REQUIRED COMPONENTS thread)

if(Boost_FOUND)
    target_include_directories(${PROJECT_ASTRA} PUBLIC
                                ${CMAKE_SOURCE_DIR}/include
                                ${CMAKE_SOURCE_DIR}/lib/include
                                PRIVATE
                                ${Boost_INCLUDE_DIRS})

    target_compile_definitions(${PROJECT_ASTRA} PRIVATE
                                ASTRA_CUDA
                                __SSE2__
                                DLL_EXPORTS
                                _CRT_SECURE_NO_WARNINGS
                                )

    target_link_libraries(${PROJECT_ASTRA}
                                Boost::disable_autolinking
                                Boost::thread
                                CUDA::cudart
                                CUDA::cufft)
    #set_target_properties(${PROJECT_ASTRA} PROPERTIES
    #                            CUDA_SEPARABLE_COMPILATION ON)

    set_target_properties(${PROJECT_ASTRA} PROPERTIES CUDA_ARCHITECTURES "70")

endif()


install(TARGETS ${PROJECT_ASTRA}
        EXPORT ${PROJECT_ASTRA}Targets
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
        RUNTIME DESTINATION bin
        )

#install(TARGETS ${PROJECT_ASTRA}
#        CONFIGURATIONS Debug
#        RUNTIME DESTINATION Debug/bin
#        LIBRARY DESTINATION Debug/lib)

#install(TARGETS ${PROJECT_ASTRA}
#        CONFIGURATIONS Release
#        RUNTIME DESTINATION Release/bin
#        LIBRARY DESTINATION Release/lib)