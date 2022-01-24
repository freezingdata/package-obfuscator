# package-obfuscator

## Quick-Start

To install the package-obfuscator run the following command:

```
pip install package-obfuscator
```

To use the package-obfuscator either use the cli:

```
package-obfuscate my_secret_package
```

To use the package-obfuscator in a script:

```python
import os
import package_obfuscator

current_folder = os.path.dirname(os.path.realpath(__file__))
package_folder = os.path.join(current_folder, 'my_secret_package')

package_obfuscator.obfuscate(package_folder)
```

## CLI

The CLI provides the following options

| Argument                        | Description                                                                                                                                                                                                |            Default |
| :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -----------------: |
| `package_location` (positional) | An absolute or relative path to the package that should be obfuscated                                                                                                                                      |           required |
| `--output` / `-o`               | An absolute or relative path to a folder in which to place the obfuscated package content. If this argument is not provided the obfuscation will take place in the originally provided `package_location`. | `package_location` |
| `--force-overwrite` / `-f`      | If the output folder is existent the obfuscator will exit. You can disable this behaviour and achieve an hard overwrite if you add this option                                                             |                    |

## Python API

### `package_obfuscator`

`package_obfuscator.obfuscate(package_dir, [output=..., [force_output_overwrite=False]])`

| Argument                 | Description                                                                                                                                                                   | Required / Optional |
| :----------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| `package_dir`            | The absolute or relative path to the package directory.                                                                                                                       | Required            |
| `output`                 | The absolute or relative path to the directory in which to place the obfuscated files. If not provided the obfuscation will take place within the `package_dir`.              | Optional            |
| `force_output_overwrite` | If the output folder exists when running the code the obfuscator will exit with an exception. If you want to force an overwrite you should provide this argument with `True`. | Optional            |

## When to use the `package-obfuscator`

The `package-obfuscator` should be used prior to releasing your python package in any way. The easiest way is to use the following code structure. Let's assume you are developing a module called `my_module`. Your directory structure will look something like this:

```
my-module-repository
  > my_module_source
      > sub_module
          script2.py
      __init__.py
      script1.py
  setup.py
```

Then it is suggested to use the `package-obfuscator` as a package in the `setup.py`.

```python
import package_obfuscator
package_obfuscator.obfuscate('my_module_source', output='my_module')

setup(
    name='my_module',
    version='0.0.1',
    packages=find_packages(include=['my_module', 'my_module.*'])
)
```

Your wheel will then only include obfuscated code.

## How does the obfuscation work?

The obfuscation works by compiling the code within each package-related python file into binary code. The binary code is then saved into separate files. The original file will execute the binary file using the `exec` command and the `marshal` library.

## How safe is the obfuscation method?

It is important to note that the obfuscation is not completely possible. It is possible to reverse-engineer your code using the binary files. But even when converting the code back only excerpts of the code will be humanly readable straight away. This method of obfuscation is recommended for code that is not mission-critical but should nevertheless not be deployed as human-readable code.
