# Module
Module is the base unit of code organization in Move. Modules are used to group and isolate code, and all of the members of the module are private to the module by default. In this section you will learn how to define a module, how to declare its members and how to access them from other modules.

## Module declaration
Modules are declared using the **module** keyword followed by the package address, module name and the module body inside the curly braces **{}**. The module name should be in snake_case - all lowercase letters with underscores between words. Modules names must be unique in the package.

Usually, a single file in the **sources/** */ folder contains a single module. The file name should match the module name - for example, a **donut_shop** module should be stored in the **donut_shop.move** file. You can read more about coding conventions in the [Coding Conventions](https://move-book.com/special-topics/coding-conventions.html) section.

