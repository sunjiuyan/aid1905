# git使用

[TOC]

## 什么是git，什么是github

Git 是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。
Git 是Linus Torvalds 为了帮助管理Linux内核开发而开发的一个开放源码的版本控制软件。

gitHub是一个面向开源及私有软件项目的托管平台，因为只支持git作为唯一的版本库格式进行托管，故名gitHub。gitHub于2008年4月10日正式上线，除了git代码仓库托管及基本的 Web管理界面以外，还提供了订阅、讨论组、文本渲染、在线文件编辑器、协作图谱（报表）、代码片段分享（Gist）等功能。

### git特点

*1.* git可以管理各种文件（但是只能对比出文本文件的变化情况而不是修改文件）。

*2.* 是分布式管理（每台机子都是一个存储站，可以在不联网情况下工作），不同于svn的集中式管理。这是GIT和其它非分布式的版本控制系统最核心的区别。

*3.*IT分支和SVN的分支不同：分支在SVN中一点不特别，就是版本库中的另外的一个目录。

*4.* GIT没有一个全局的版本号，而SVN有：目前为止这是跟SVN相比GIT缺少的最大的一个特征。

*5.* GIT的内容完整性要优于SVN：GIT的内容存储使用的是SHA-1哈希算法。这能确保代码内容的完整性，确保在遇到磁盘故障和网络问题时降低对版本库的破坏。

*6.* GIT把内容按元数据方式存储，而SVN是按文件：所有的资源控制系统都是把文件的元信息隐藏在一个类似.svn,.cvs等的文件夹里。

## git 安装

最早Git是在Linux上开发的，很长一段时间内，Git也只能在Linux和Unix系统上跑。不过，慢慢地有人把它移植到了Windows上。现在，Git可以在Linux、Unix、Mac和Windows这几大平台上正常运行了。

### Linux 平台安装

如果你用Debian或Ubuntu Linux通过
`sudo apt-get install git` 就可以直接完成Git的安装。

### Windows 平台安装

在 Windows 平台上安装 Git 同样轻松，有个叫做 msysGit 的项目提供了安装包，可以到 GitHub 的页面上下载 exe 安装文件并运行：
安装包下载地址：[http://msysgit.github.io/](http://msysgit.github.io/)

安装后可以使用 `git --version` 查看版本信息。

### git 基本配置

Git 提供了一个叫做 git config 的工具，专门用来配置或读取相应的工作环境变量。
这些环境变量，决定了Git在各个环节的具体工作方式和行为。在做基本操作之前必须要进行这些基本配置。这些配置变量可以存放在以下三个不同的地方：

* `/etc/gitconfig` 文件：系统中对所有用户都普遍适用的配置。若使用 git config 时用 --system 选项，读写的就是这个文件。

* `~/.gitconfig` 文件：用户目录下的配置文件只适用于该用户。若使用 git config 时用 --global 选项，读写的就是这个文件。

* 当前项目的 Git 目录中的配置文件（也就是工作目录中的 `.git/config` 文件）：也就是git config 不加任何选项，这样的配置仅仅针对当前项目有效。

每一个级别的配置都会覆盖上层的相同配置，所以 `.git/config` 里的配置会覆盖 /etc/gitconfig 中的同名变量。

* 用户名

`git config --global  user.name  [yourname]`

* 邮箱

`git config --global  user.email  [youremail]`

* 编辑器设置

`git config --global  core.editor  [youreditor]`

* 检查已有的配置信息

`git config --list`

* 命令起别名

`git config --global alias.st status`   将status命令起别名为st 

如果要删除alias配置则只需要到主目录的.gitconfig 文件中将对应的配置行去掉即可

* 忽略文件

在git仓库中有时候不需要把所有文件都进行协同操作。创建.gitignore文件夹，把忽略的文件名添加进去，这样在同步的时候就不会自动上传。


git常用的命令如下，我们分为基本操作，版本控制，分支控制，标签管理和远程仓库操作基本分分别涉及这些命令：

```
   add        添加文件内容至索引
   bisect     通过二分查找定位引入 bug 的变更
   branch     列出、创建或删除分支
   checkout   检出一个分支或路径到工作区
   clone      克隆一个仓库到一个新目录
   commit     记录变更到仓库
   diff       显示提交之间、提交和工作区之间等的差异
   fetch      从另外一个仓库下载对象和引用
   grep       输出和模式匹配的行
   init       创建一个空的 Git 仓库或重新初始化一个已存在的仓库
   log        显示提交日志
   merge      合并两个或更多开发历史
   mv         移动或重命名一个文件、目录或符号链接
   pull       获取并整合另外的仓库或一个本地分支
   push       更新远程引用和相关的对象
   rebase     本地提交转移至更新后的上游分支中
   reset      重置当前 HEAD 到指定状态
   rm         从工作区和索引中删除文件
   show       显示各种类型的对象
   status     显示工作区状态
   tag        创建、列出、删除或校验一个 GPG 签名的标签对象
```

## git的基本命令

* 初始化仓库

`git init`     

* 添加跟踪文件，提交到缓存，可以是多个，逗号隔开

`git  add  filenames`   

* 提交文件，将文件修改提交到仓库。可以是多个 提交时添加提交日志

`git  commit  -m  “some message”`   

* 查看仓库状态

`git  status`  

* 查看修改信息

`git log`

* 修改文件后,查看改动内容。后面可以跟一个文件作为参数，这个命令基本和linux  diff命令相同，不跟比较目录下所有的文件

`git diff file1`

* 删除文件

`git  rm filename`

之后执行commit则文件确认删除

如果发现误删了用下面命令恢复：

`git checkout  filename`

* 移动文件

`git  mv  file1  dir`

基本操作和rm类似

## 版本控制 

* 回到了老版本

`git reset  --hard  HEAD^`   

回到上一个版本 几个 ^ 表示回到上几个版本 ，如果超过10可以用HEAD~10 表示回到上10个版本

* 去往较新的版本

git log命令查看修改信息其中commit行会提供被我们一个版本编号，通过它可以帮助我们选择回复到哪个版本，如果不想显示具体修改内容可以用

`git log --pretty=oneline`

`git reset --hard  [commt_id]`

这样如果没有关界面那么在上面的git log命令中可以查看commt_id，用前7位就行 
如果界面已经关了，就需要git reflog命令查看之前版本的ID （因为git  log命令只显示比当前版本旧的ID，不会显示出比当前版本新的操作记录），这个命令记录操作记录

* 查看工作区文件（filename）和仓库中最新版本的差异

`git  diff HEAD -- filename`   

* 丢弃工作区的修改

`git checkout -- file`

```
$ git checkout -- readme.txt
```

这个命令的意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情况：
一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

用命令`git reset HEAD file`可以把暂存区的修改撤销掉，重新放回工作区。

* 创建临时保存工作区

`git  stash`    

在工作修改了但是还没有add commit的情况下，如果已经提交就没必要了。

* 显示工作取列表

`git  stash  list`   

* 回复保存的工作区

`git  stash  apply   stash@｛0｝`

* 删除保存工作区

`git  stash drop  stash@｛0｝` 

* 回复并删除保存的工作区

`git stash pop` 

* 删除所有stash工作区

'git stash clear'

## 分支管理

### 什么是分支

几乎每一种版本控制系统都以某种形式支持分支。使用分支意味着你可以从开发主线上分离开来，然后在不影响主线的同时继续工作。假设你准备开发一个新功能，但是需要两周才能完成，第一周你写了50%的代码，如果立刻提交，由于代码还没写完，不完整的代码库会导致别人不能干活了。如果等代码全部写完再一次提交，又存在丢失每天进度的巨大风险。现在有了分支,你创建了一个属于你自己的分支，别人看不到，还继续在原来的分支上正常工作，而你在自己的分支上干活，想提交就提交，直到开发完毕后，再一次性合并到原来的分支上，这样，既安全，又不影响别人工作。

* 查看当前分支  有 `*` 的为当前作用分支

`git branch`

* 创建一个叫dev的分支

`git  branch  dev`

* 切换到 dev分支

`git  checkout  dev`    

上两个命令 可以用  `git  checkout  -b  dev`  完成。

* 合并dev分支到当前分支  快速合并

`git  merge dev` 

* 删除dev分支

`git branch  -d  dev`

* 强行删除分支
     
`git branch -D dev`

如果分支没有合并默认是不允许用-d的命令删除的，而这个命令可以。

* 分支合并图
 
`git log --graph`

* 进行普通合并

`git merge --no-ff -m "merge with no-ff" dev`  


## 标签管理

### 什么是标签

如果你达到一个重要的阶段，并希望永远记住那个特别的提交快照，你可以使用 git tag 给它打上标签。Git的标签虽然是版本库的快照，但其实它就是指向某个commit的指针，这跟分支很像，但是分支可以移动，标签不能移动，所以，创建和删除标签都是瞬间完成的。

选择要打标签的分支后进行如下操作：

git  tag  v1.0   打一个v1.0的标签，默认打在最新的commit上

git  tag  v0.9    6224637    打在对应的commit_id上

git  tag  查看标签

git  show   v1.0  查看标签commit的具体内容

还可以创建带有说明的标签，用-a指定标签名，-m指定说明文字：

git tag -a v0.1 -m "version 0.1 released"3628164

git tag -d v0.1  删除标签

git  reset  --hard    v1.0  回复到v1.0标签状态

## 远程仓库操作

### 创建仓库

初始化Git仓库
首先我们选定一个目录作为Git仓库，假定是/home/gitrepo/runoob.git，在/home/gitrepo目录下输入命令：
$ cd /home
$ mkdir gitrepo
$ chown linux:linux gitrepo/
$ cd gitrepo

$ git init --bare runoob.git
Initialized empty Git repository in /home/gitrepo/runoob.git/
以上命令Git创建一个空仓库，服务器上的Git仓库通常都以.git结尾。然后，把仓库所属用户改为linux：
$ chown -R linux:linux runoob.git


添加远程仓库

如果我们现在本地有一个git仓库, 我们使用remote add 命令将它添加到远程的仓库中.
$ git remote add origin linux@127.0.0.1:/home/linux/gitrepo/runoob.git


并需要将远程的仓库的信息更步到本地,这里主要指的示远程仓库的分支和远程库的提交变更信息。这种方法使用的是git协议 使用自己的用户名，然后冒号后是github对应仓库路径。使用ssh登录，第一次会有个警告提示。这种方法需要先建立ssh密钥方式的链接。

$ git fetch origin

* 与git pull相比git fetch相当于是从远程获取最新版本到本地，但不会自动merge。如果需要有选择的合并git fetch是更好的选择。效果相同时git pull将更为快捷。

向远程仓库提交基本操作

同步master分支
同步其它分支
同步远程标签
删除远程分支
删除远程标签
同步master分支

如果我们本地的仓库进行开发, 交进行提交commit. 那么我们本地的仓库和远程的仓库就不能保持同步了.那么我们需要把本地的这次提交也要反映在远程的仓库上. 那么我们就需要使用push命令.

$ git push origin master

注意 ： 第一次同步时仓库为空使用 `git push -u  origin master `

* 同步其它分支

如果我们需要我们其它分支的提交也要反映在远程库中. 如果远程没有这个分支, 它就会自动创建这个分支.

$ git push origin branch-name

* 同步标签

使用git push origin branch-name命令不会将本地打好的标签同步(推送)到服务器上, 需要使用下面的命令将本地的tags同步(推送)到服务器上.

git push origin --tags  推送所有标签

git push origin v1.0 推送标签到远程


删除远程分支

可以用这个非常有意思的语法来删除它：git push [远程名] :[分支名]。 在于分支名前的冒号.

$ git push -u origin :branch-name


删除远程标签

如果我们也想把远程仓库中是的标签删除.

$ git push origin --delete <branchName>
$ git push origin --delete tag <tagname>

###  从远程仓库同步

clone

当我们知道git仓库的地址了(在github上有很多的开源仓库.), 就可以使用下面的命令将源码拉取到本地.

$ git clone url

e.g. 
$ git clone linux@127.0.0.1:/home/linux/gitrepo/runoob.git

pull

我们已经拉取源码到本地了,但是服务器上的git已经更新了,当我们需要将服务器的源码与本地源友进行同步进时, 需要使用下面的命令.

$ git pull
 


### 与github仓库协同

* 同步本地仓库到github 

`git remote add origin git@github.com:michaelliao/learngit.git`

* 将本地代码同步到github

`git  push  origin master`

如果同步时你不是origin中最新版本则需要先pull



### 将github仓库同步到本地

* 将远程仓库同步到本地

`git  clone git@github.com:michaelliao/learngit.git`  对标 git  remote add 

* 将仓库中的代码拉到本地 

`git  pull  origin master`   对标git  push命令，

注意：

*1.*  git支持多种协议，可以登录后从本地直接上传也可以，可以复制地址，那么可以用下面的命令:
`git remote add origin https://github.com:michaelliao/learngit.git` 但是这样写后面需要输入用户名和密码才能push，pull。

*2.*  origin是自己取得远程库的名字统一分支不能重复，可以用`git remote` 查看，`git  remote rm  origin`可以删除。

*3.*  `git fetch origin`可以将远程库信息同步到本地和pull区别是这个命令先不合并。如果不确定修改内容可先用这个命令进行对比，而不是直接pull

* 将远程同步到本地命名为tmp 

`git fetch origin master:tmp`

* 查看tmp和本地当前分支区别   

`git diff tmp` 

* 合并到本地分支                    

`git merge tmp`                     




