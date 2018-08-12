from enum import Enum
import numpy as np

# https://sites.uni.edu/morgans/astro/course/Notes/section2/spectraltemps.html
class SpectralType(Enum):
    # Dwarfs
    O5V = {'name': 'O5V', 'Teff': 54000, 'M': -4.5, 'L': 200000}
    O6V = {'name': 'O6V', 'Teff': 45000, 'M': -4.0, 'L': 140000}
    O7V = {'name': 'O7V', 'Teff': 43300, 'M': -3.9, 'L': 120000}
    O8V = {'name': 'O8V', 'Teff': 40600, 'M': -3.8, 'L': 80000}
    O9V = {'name': 'O9V', 'Teff': 37800, 'M': -3.6, 'L': 55000}
    B0V = {'name': 'B0V', 'Teff': 29200, 'M': -3.3, 'L': 24000}
    B1V = {'name': 'B1V', 'Teff': 23000, 'M': -2.3, 'L': 5550}
    B2V = {'name': 'B2V', 'Teff': 21000, 'M': -1.9, 'L': 3190}
    B3V = {'name': 'B3V', 'Teff': 17600, 'M': -1.1, 'L': 1060}
    B5V = {'name': 'B5V', 'Teff': 15200, 'M': -0.4, 'L': 380}
    B6V = {'name': 'B6V', 'Teff': 14300, 'M': 0, 'L': 240}
    B7V = {'name': 'B7V', 'Teff': 13500, 'M': 0.3, 'L': 140}
    B8V = {'name': 'B8V', 'Teff': 12300, 'M': 0.7, 'L': 73}
    B9V = {'name': 'B9V', 'Teff': 11400, 'M': 1.1, 'L': 42}
    A0V = {'name': 'A0V', 'Teff': 9600, 'M': 1.5, 'L': 24}
    A1V = {'name': 'A1V', 'Teff': 9330, 'M': 1.7, 'L': 20}
    A2V = {'name': 'A2V', 'Teff': 9040, 'M': 1.8, 'L': 17}
    A3V = {'name': 'A3V', 'Teff': 8750, 'M': 2.0, 'L': 14}
    A4V = {'name': 'A4V', 'Teff': 8480, 'M': 2.1, 'L': 12}
    A5V = {'name': 'A5V', 'Teff': 8310, 'M': 2.2, 'L': 11}
    A7V = {'name': 'A7V', 'Teff': 7920, 'M': 2.4, 'L': 8.8}
    F0V = {'name': 'F0V', 'Teff': 7350, 'M': 3.0, 'L': 5.1}
    F2V = {'name': 'F2V', 'Teff': 7050, 'M': 3.3, 'L': 3.8}
    F3V = {'name': 'F3V', 'Teff': 6850, 'M': 3.5, 'L': 3.2}
    F5V = {'name': 'F5V', 'Teff': 6700, 'M': 3.7, 'L': 2.7}
    F6V = {'name': 'F6V', 'Teff': 6550, 'M': 4.0, 'L': 2.0}
    F7V = {'name': 'F7V', 'Teff': 6400, 'M': 4.3, 'L': 1.5}
    F8V = {'name': 'F8V', 'Teff': 6300, 'M': 4.4, 'L': 1.4}
    G0V = {'name': 'G0V', 'Teff': 6050, 'M': 4.7, 'L': 1.2}
    G1V = {'name': 'G1V', 'Teff': 5930, 'M': 4.9, 'L': 1.1}
    G2V = {'name': 'G2V', 'Teff': 5800, 'M': 5.0, 'L': 1}
    G5V = {'name': 'G5V', 'Teff': 5660, 'M': 5.2, 'L': 0.73}
    G8V = {'name': 'G8V', 'Teff': 5440, 'M': 5.6, 'L': 0.51}
    K0V = {'name': 'K0V', 'Teff': 5240, 'M': 6.0, 'L': 0.38}
    K1V = {'name': 'K1V', 'Teff': 5110, 'M': 6.2, 'L': 0.32}
    K2V = {'name': 'K2V', 'Teff': 4960, 'M': 6.4, 'L': 0.29}
    K3V = {'name': 'K3V', 'Teff': 4800, 'M': 6.7, 'L': 0.24}
    K4V = {'name': 'K4V', 'Teff': 4600, 'M': 7.1, 'L': 0.18}
    K5V = {'name': 'K5V', 'Teff': 4400, 'M': 7.4, 'L': 0.15}
    K7V = {'name': 'K7V', 'Teff': 4000, 'M': 8.1, 'L': 0.11}
    M0V = {'name': 'M0V', 'Teff': 3750, 'M': 8.7, 'L': 0.080}
    M1V = {'name': 'M1V', 'Teff': 3700, 'M': 9.4, 'L': 0.055}
    M2V = {'name': 'M2V', 'Teff': 3600, 'M': 10.1, 'L': 0.035}
    M3V = {'name': 'M3V', 'Teff': 3500, 'M': 10.7, 'L': 0.027}
    M4V = {'name': 'M4V', 'Teff': 3400, 'M': 11.2, 'L': 0.022}
    M5V = {'name': 'M5V', 'Teff': 3200, 'M': 12.3, 'L': 0.011}
    M6V = {'name': 'M6V', 'Teff': 3100, 'M': 13.4, 'L': 0.0051}
    M7V = {'name': 'M7V', 'Teff': 2900, 'M': 13.9, 'L': 0.0032}
    M8V = {'name': 'M8V', 'Teff': 2700, 'M': 14.4, 'L': 0.0020}
    L0V = {'name': 'L0V', 'Teff': 2600, 'M': np.inf, 'L': 0.00029}
    L3V = {'name': 'L3V', 'Teff': 2200, 'M': np.inf, 'L': 0.00013}
    L8V = {'name': 'L8V', 'Teff': 1500, 'M': np.inf, 'L': 0.000032}
    T2V = {'name': 'T2V', 'Teff': 1400, 'M': np.inf, 'L': 0.000025}
    T6V = {'name': 'T6V', 'Teff': 1000, 'M': np.inf, 'L': 0.0000056}
    T8V = {'name': 'T8V', 'Teff': 800, 'M': np.inf, 'L': 0.0000036}

    # Giants
    G5III = {'name': 'G5III', 'Teff': 5010, 'M': 0.7, 'L': 127}
    G8III = {'name': 'G8III', 'Teff': 4870, 'M': 0.6, 'L': 113}
    K0III = {'name': 'K0III', 'Teff': 4720, 'M': 0.5, 'L': 96}
    K1III = {'name': 'K1III', 'Teff': 4580, 'M': 0.4, 'L': 82}
    K2III = {'name': 'K2III', 'Teff': 4460, 'M': 0.2, 'L': 70}
    K3III = {'name': 'K3III', 'Teff': 4210, 'M': 0.1, 'L': 58}
    K4III = {'name': 'K4III', 'Teff': 4010, 'M': 0.0, 'L': 45}
    K5III = {'name': 'K5III', 'Teff': 3780, 'M': -0.2, 'L': 32}
    M0III = {'name': 'M0III', 'Teff': 3660, 'M': -0.4, 'L': 15}
    M1III = {'name': 'M1III', 'Teff': 3600, 'M': -0.5, 'L': 13}
    M2III = {'name': 'M2III', 'Teff': 3500, 'M': -0.6, 'L': 11}
    M3III = {'name': 'M3III', 'Teff': 3300, 'M': -0.7, 'L': 9.5}
    M4III = {'name': 'M4III', 'Teff': 3100, 'M': -0.75, 'L': 7.4}
    M5III = {'name': 'M5III', 'Teff': 2950, 'M': -0.8, 'L': 5.1}
    M6III = {'name': 'M6III', 'Teff': 2800, 'M': -0.9, 'L': 3.3}

    # Supergiants
    B0I = {'name': 'B0I', 'Teff': 21000, 'M': -6.4, 'L': 320000}
    B1I = {'name': 'B1I', 'Teff': 16000, 'M': -6.4, 'L': 280000}
    B2I = {'name': 'B2I', 'Teff': 14000, 'M': -6.4, 'L': 220000}
    B3I = {'name': 'B3I', 'Teff': 12800, 'M': -6.3, 'L': 180000}
    B5I = {'name': 'B5I', 'Teff': 11500, 'M': -6.3, 'L': 140000}
    B6I = {'name': 'B6I', 'Teff': 11000, 'M': -6.3, 'L': 98000}
    B7I = {'name': 'B7I', 'Teff': 10500, 'M': -6.3, 'L': 82000}
    B8I = {'name': 'B8I', 'Teff': 10000, 'M': -6.2, 'L': 73000}
    B9I = {'name': 'B9I', 'Teff': 9700, 'M': -6.2, 'L': 61000}
    A0I = {'name': 'A0I', 'Teff': 9400, 'M': -6.2, 'L': 50600}
    A1I = {'name': 'A1I', 'Teff': 9100, 'M': -6.2, 'L': 44000}
    A2I = {'name': 'A2I', 'Teff': 8900, 'M': -6.2, 'L': 40000}
    A5I = {'name': 'A5I', 'Teff': 8300, 'M': -6.1, 'L': 36000}
    F0I = {'name': 'F0I', 'Teff': 7500, 'M': -6.0, 'L': 20000}
    F2I = {'name': 'F2I', 'Teff': 7200, 'M': -6.0, 'L': 18000}
    F5I = {'name': 'F5I', 'Teff': 6800, 'M': -5.9, 'L': 16000}
    F8I = {'name': 'F8I', 'Teff': 6150, 'M': -5.9, 'L': 12000}
    G0I = {'name': 'G0I', 'Teff': 5800, 'M': -5.9, 'L': 9600}
    G2I = {'name': 'G2I', 'Teff': 5500, 'M': -5.8, 'L': 9500}
    G5I = {'name': 'G5I', 'Teff': 5100, 'M': -5.8, 'L': 9800}
    G8I = {'name': 'G8I', 'Teff': 5050, 'M': -5.7, 'L': 11000}
    K0I = {'name': 'K0I', 'Teff': 4900, 'M': -5.7, 'L': 12000}
    K1I = {'name': 'K1I', 'Teff': 4700, 'M': -5.6, 'L': 13500}
    K2I = {'name': 'K2I', 'Teff': 4500, 'M': -5.6, 'L': 15200}
    K3I = {'name': 'K3I', 'Teff': 4300, 'M': -5.6, 'L': 17000}
    K4I = {'name': 'K4I', 'Teff': 4100, 'M': -5.5, 'L': 18300}
    K5I = {'name': 'K5I', 'Teff': 3750, 'M': -5.5, 'L': 20000}
    M0I = {'name': 'M0I', 'Teff': 3660, 'M': -5.3, 'L': 50600}
    M1I = {'name': 'M1I', 'Teff': 3600, 'M': -5.3, 'L': 52000}
    M2I = {'name': 'M2I', 'Teff': 3500, 'M': -5.3, 'L': 53000}
    M3I = {'name': 'M3I', 'Teff': 3300, 'M': -5.3, 'L': 54000}
    M4I = {'name': 'M4I', 'Teff': 3100, 'M': -5.2, 'L': 56000}
    M5I = {'name': 'M5I', 'Teff': 2950, 'M': -5.2, 'L': 58000}

def getSpectralTypeInformation(spt: SpectralType) -> str:
    spectral = spt.value['name']
    teff = spt.value['Teff']
    return f'Spectral type: {spectral}: Teff={teff}K'


if __name__ == '__main__':
    print(getSpectralTypeInformation(SpectralType.M5V))
