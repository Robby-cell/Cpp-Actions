from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class CppActionsRecipe(ConanFile):
    name = "cpp-actions"
    version = "0.1"
    package_type = "application"

    # Optional metadata
    license = "MIT"
    author = "Robert Williamson"
    url = "https://github.com/Robby-cell/Cpp-Actions"
    description = "Using Github Actions with C++ and Conan2"
    topics = ("Git", "Github", "C++", "Conan", "Automation")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    

    
