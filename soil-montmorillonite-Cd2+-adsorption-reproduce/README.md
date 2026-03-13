# 蒙脱石吸附Cd²⁺的界面机理研究（DFT+MD）- 可重复研究项目
本项目为**土壤界面吸附+计算化学**方向的可重复研究作业，基于MDPI期刊《Processes》2022年的论文展开，核心还原论文中的DFT计算和MD模拟流程，实现研究的可复现性。

## 一、论文核心信息
- 标题：Understanding Cd²⁺ Adsorption Mechanism on Montmorillonite Surfaces by Combining DFT and MD
- 作者：Jia Du, Qinghe Wang, Jun Chen
- 期刊：Processes, 2022, 10(7): 1381
- DOI：[10.3390/pr10071381](https://doi.org/10.3390/pr10071381)
- 研究方法：密度泛函理论（DFT）+ 分子动力学（MD）
- 核心结论：蒙脱石(010)表面对Cd²⁺的吸附能（-283.55 kJ/mol）远高于(001)表面（-88.74 kJ/mol）；Cd²⁺在(001)表面为静电吸附，(010)表面为共价键吸附。

## 二、项目目录结构
## 三、可复现性说明
本项目基于**计算流程复现+环境固化**实现研究可重复，因Materials Studio为商业软件，暂未提供原软件输入文件，核心可复现点如下：
1. **参数可复现**：从论文中精准提取DFT/MD的所有核心计算参数，可直接用于Materials Studio复现计算；
2. **公式可复现**：编写Python脚本实现论文的吸附能计算公式，可直接运行并修改参数；
3. **环境可复现**：通过renv和pip固化R/Python环境，确保数据分析环境一致；
4. **结论可复现**：基于论文参数和公式，可重复得到Cd²⁺在蒙脱石表面的吸附规律。

## 四、环境还原方法
### 4.1 Python环境还原（基于requirements.txt）
使用uv/pip安装依赖，确保版本一致：
```bash
# 激活虚拟环境后执行
uv pip install -r env/requirements.txt
# 或使用pip
pip install -r env/requirements.txt