find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_OWC gnuradio-owc)

FIND_PATH(
    GR_OWC_INCLUDE_DIRS
    NAMES gnuradio/owc/api.h
    HINTS $ENV{OWC_DIR}/include
        ${PC_OWC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_OWC_LIBRARIES
    NAMES gnuradio-owc
    HINTS $ENV{OWC_DIR}/lib
        ${PC_OWC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-owcTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_OWC DEFAULT_MSG GR_OWC_LIBRARIES GR_OWC_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_OWC_LIBRARIES GR_OWC_INCLUDE_DIRS)
