from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout

class Cmp2Conan(ConanFile):
    name = "cmp2"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("cmp1/0.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure(variables = {"CMAKE_VERBOSE_MAKEFILE":True})
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
