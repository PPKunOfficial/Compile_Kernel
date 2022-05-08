# Compile Kernel
## Use GitHub actions to compile your kernel source code

##  This workflow is only applicable to kernel source code compiled in GitHub

In order to speed up the speed of pulling code, in the workflow files uses `checkout` to pull code instead of `git clone`


As a result, you can only pull the source code in GitHub, not the external one. If necessary, the version pulled by `git clone` will be released later

## Parameter interpretation
| Parameter name | Parameter description | Example |
| ------------ | -------------------- | ------------ |
| `AUTHOR` | The author of the repo | PPKunOfficial |
| `CHECKOUT_REPO` | Repository to pull | android_kernel_xiaomi_sdm845 |
| `CHECKOUT_BRANCH` | Branch of Repository | rebase-s |
| `USEDEFCONFIG` | Defconfig used for compilation | dipper_defconfig |
| `USE_LANZOU` | Use Lanzou Cloud `1` for use | 1 |
| `LANZOU_COOKIE_YLOGIN` | Lanzou cookie of ylogin(Just Number) | 114514 |
| `LANZOU_COOKIE_PHPDISKINFO` | Lanzou cookie of phpdisk_info(There are characters and numbers) | 114514tshe1919810c |

## Notice: If you don't upload to Lanzou cloud, please `USE_LANZOU` is set to 0 (false), and the following Lanzou cloud cookie for login does not need to be filled in. If Laznou is not used, it will be uploaded to `release`

## Examples for Lanzou

![Lanzou_Cloud](https://raw.githubusercontent.com/PPKunOfficial/Compile_Kernel/main/lanzou_example.png)