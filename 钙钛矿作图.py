import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import gaussian
from matplotlib.patches import Polygon

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建波长范围
wavelength = np.linspace(400, 700, 500)  # nm
energy = 1240 / wavelength  # 转换为eV


# 定义更真实的钙钛矿吸收光谱（包含带边吸收和高能连续吸收）
def perovskite_absorption_spectrum(energy):
    # 带边吸收（高斯峰）
    band_edge_center = 2.7  # eV
    band_edge_width = 0.1
    band_edge = np.exp(-((energy - band_edge_center) / band_edge_width) ** 2)

    # 高能连续吸收（指数衰减背景）
    #high_energy_bg = 0.3 * np.exp((energy - 2.4) / 0.5)  # 从低能到高能衰减
    #high_energy_bg = np.exp(-((energy - 3.2) / 0.4) ** 2)

    # 合并吸收特征
    absorption = band_edge #+ high_energy_bg


    return absorption / np.max(absorption)  # 归一化


# 生成吸收光谱
absorption_spectrum = perovskite_absorption_spectrum(energy)

# 定义自由激子发射光谱
free_exciton_center = 2.6  # eV，小的斯托克斯位移
free_exciton_width = 0.12
free_exciton_emission = np.exp(-((energy - free_exciton_center) / free_exciton_width) ** 2)

# 定义自陷态发射光谱
self_trapped_center = 2.1  # eV，大的斯托克斯位移
self_trapped_width = 0.2
self_trapped_emission = np.exp(-((energy - self_trapped_center) / self_trapped_width) ** 2)

# 混合发射光谱 (自由激子 + 自陷态)
mixed_emission = 0.3 * free_exciton_emission + 0.7 * self_trapped_emission
mixed_emission = mixed_emission / np.max(mixed_emission)  # 归一化

# 归一化发射光谱
free_exciton_emission = free_exciton_emission / np.max(free_exciton_emission)
self_trapped_emission = self_trapped_emission / np.max(self_trapped_emission)

# 创建图形
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 子图1: 纯自由激子情况
ax1.plot(energy, absorption_spectrum, 'b-', linewidth=2.5, label='激发光谱', alpha=0.8)
ax1.plot(energy, free_exciton_emission, 'r-', linewidth=2.5, label='自由激子发射', alpha=0.8)

# 填充重叠区域
overlap_mask1 = np.minimum(absorption_spectrum, free_exciton_emission)
ax1.fill_between(energy, overlap_mask1, alpha=0.5, color='purple', label='光谱重叠区域')

ax1.set_xlabel('Energy/eV', fontsize=12)
ax1.set_ylabel('Intensity/a.u.', fontsize=12)
ax1.legend(fontsize=10)
ax1.set_xlim(1.8, 3.0)  # 扩展能量范围以显示高能吸收
ax1.set_ylim(0, 1.1)

# 添加吸收特征标注


# 子图2: 含自陷态情况
ax2.plot(energy, absorption_spectrum, 'b-', linewidth=2.5, label='激发光谱', alpha=0.8)
ax2.plot(energy, mixed_emission, 'r-', linewidth=2.5, label='含自陷态发射', alpha=0.8)


# 填充重叠区域
overlap_mask2 = np.minimum(absorption_spectrum, mixed_emission)
ax2.fill_between(energy, overlap_mask2, alpha=0.5, color='purple', label='光谱重叠区域')

ax2.set_xlabel('Energy/eV', fontsize=12)
ax2.set_ylabel('Intensity/a.u.', fontsize=12)
ax2.legend(fontsize=10)
ax2.set_xlim(1.8, 3.0)
ax2.set_ylim(0, 1.1)

# 计算并显示重叠积分（考虑λ⁴权重）
# 转换为波长进行计算：λ = 1240/energy (nm)
wavelength_calc = 1240 / energy
J_free = np.trapz(np.minimum(absorption_spectrum, free_exciton_emission) * energy**4, energy)
J_mixed = np.trapz(np.minimum(absorption_spectrum, mixed_emission) * energy**4, energy)

# 在图中添加重叠积分信息
ax1.text(0.05, 0.2, f'重叠积分 J = {-J_free:.2}', transform=ax1.transAxes,
         fontsize=11, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax2.text(0.05, 0.2, f'重叠积分 J = {-J_mixed:.2}', transform=ax2.transAxes,
         fontsize=11, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# 添加箭头标注自陷态红移和有效重叠区域
#ax2.annotate('自陷态红移', xy=(self_trapped_center, 0.8), xytext=(free_exciton_center, 0.9),
             #arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             #fontsize=10, color='red', ha='center')
#ax2.annotate('有效重叠区域', xy=(2.25, 0.3), xytext=(2.5, 0.5),
             #arrowprops=dict(arrowstyle='->', color='purple', lw=1.5),
             #fontsize=10, color='purple', ha='center')

plt.tight_layout()
plt.show()

# 打印定量比较结果
print("=" * 50)
print("钙钛矿体系光谱重叠分析")
print("=" * 50)
print(f"纯自由激子体系的重叠积分: {J_free:.2e}")
print(f"含自陷态体系的重叠积分: {J_mixed:.2e}")
print(f"重叠积分减少比例: {(1 - J_mixed / J_free) * 100:.1f}%")
print(
    f"高能连续吸收占比: {np.trapz(absorption_spectrum[energy > 2.6], energy[energy > 2.6]) / np.trapz(absorption_spectrum, energy) * 100:.1f}%")