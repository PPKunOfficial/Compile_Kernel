[Jump to English(Chinglish](https://github.com/PPKunOfficial/Compile_Kernel/blob/main/README_EN.md)
# 内核编译
## 使用Github Actions来编译你的内核源码

## Notice: 本workflows仅仅适用于编译github上的内核源码

为了加快拉取代码的速度，workflows里使用`checkout`来拉取代码而不是`git clone`

这导致只能拉取GitHub站内的源码，而不能拉取外部，有需要的后期会出`git clone`拉取的版本

## 参数解释

| 参数名 | 参数描述 | 范例 |
| ------------ | -------------------- | ------------ |
| `AUTHOR` | 源码仓库作者 | PPKunOfficial |
| `CHECKOUT_REPO` | 需拉取的仓库 | android_kernel_xiaomi_sdm845 |
| `CHECKOUT_BRANCH` | 仓库的分支 | rebase-s |
| `USEDEFCONFIG` | 编译使用的defconfig| dipper_defconfig |
| `USE_LANZOU` | 是否使用蓝奏云 `1`为使用 | 1 |
| `LANZOU_COOKIE_YLOGIN` | 蓝奏云cookie ylogin(纯数字) | 114514 |
| `LANZOU_COOKIE_PHPDISKINFO` | 蓝奏云cookie phpdisk_info | 114514tshe1919810c |

## Notice: 若不上传到蓝奏云，请将`USE_LANZOU`设置为0(`false`)，然后下面用于登陆的蓝奏云cookie不需要填写。如果不使用蓝奏，将会上传到`Release`

## 蓝奏云cookie样例

![蓝奏云](https://raw.githubusercontent.com/PPKunOfficial/Compile_Kernel/main/lanzou_example.png)