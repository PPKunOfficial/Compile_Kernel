[Jump to English(Chinglish](https://github.com/PPKunOfficial/Compile_Kernel/blob/main/README_EN.md)
# 内核编译
## 使用Github Actions来编译你的内核源码

## Notice: 本workflows仅仅适用于编译github上的内核源码

为了加快拉取代码的速度，workflows里使用`checkout`来拉取代码而不是`git clone`

这导致只能拉取GitHub站内的源码，而不能拉取外部，有需要的后期会出`git clone`拉取的版本

## 参数解释

| 参数名                      | 参数描述                    | 范例                         |
| --------------------------- | --------------------------- | ---------------------------- |
| `AUTHOR`                    | 源码仓库作者                | PPKunOfficial                |
| `CHECKOUT_REPO`             | 需拉取的仓库                | android_kernel_xiaomi_sdm845 |
| `CHECKOUT_BRANCH`           | 仓库的分支                  | rebase-s                     |
| `USEDEFCONFIG`              | 编译使用的defconfig         | dipper_defconfig             |
| `USE_LANZOU`                | 是否使用蓝奏云 `1`为使用    | 1                            |
| `LANZOU_COOKIE_YLOGIN`      | 蓝奏云cookie ylogin(纯数字) | 114514                       |
| `LANZOU_COOKIE_PHPDISKINFO` | 蓝奏云cookie phpdisk_info   | 114514tshe1919810c           |

## Notice: 若不上传到蓝奏云，请将`USE_LANZOU`设置为0(`false`)，然后下面用于登陆的蓝奏云cookie不需要填写。如果不使用蓝奏，将会上传到`Release`

## 蓝奏云cookie样例

<img src='data:img/jpg;base64,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
b0oSua8NMQAAAABJRU5ErkJggg=='/>