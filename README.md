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

The use the package-obfuscator in a script:

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
