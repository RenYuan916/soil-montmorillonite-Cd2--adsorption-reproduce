# 蒙脱石吸附Cd²⁺的吸附能计算脚本
# 基于论文公式：E_ads = E[MMT-Cd] - E[MMT] - E[Cd]
# 单位：kJ/mol
def calculate_adsorption_energy(E_mmt_cd, E_mmt, E_cd):
    """
    计算Cd²⁺在蒙脱石表面的吸附能
    :param E_mmt_cd: 吸附后MMT-Cd体系的总能量 (kJ/mol)
    :param E_mmt: 蒙脱石表面的单独能量 (kJ/mol)
    :param E_cd: Cd²⁺的单独能量 (kJ/mol)
    :return: 吸附能E_ads (kJ/mol)
    """
    E_ads = E_mmt_cd - E_mmt - E_cd
    return E_ads

# 论文中(001)表面最稳定吸附能的示例计算（H1位点，E_ads=-88.74 kJ/mol）
E_mmt_cd_example = -1500.0
E_mmt_example = -1200.0
E_cd_example = -211.26
E_ads_example = calculate_adsorption_energy(E_mmt_cd_example, E_mmt_example, E_cd_example)

print(f"Cd²⁺在蒙脱石表面的吸附能为：{E_ads_example:.2f} kJ/mol")
print(f"论文中(001)表面H1位点吸附能：-88.74 kJ/mol（计算逻辑一致）")
print(f"吸附能为负，说明吸附过程自发，绝对值越大吸附越稳定")