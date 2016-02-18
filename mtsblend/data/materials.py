# -*- coding: utf8 -*-
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
# --------------------------------------------------------------------------
# Blender Mitsuba Add-On
# --------------------------------------------------------------------------
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# ***** END GPL LICENSE BLOCK *****

conductor_material_items = [
    ('', 'Choose Material Preset', ''),
    ('custom', 'Custom Values', 'custom'),
    ('none', '100% Pure Mirror', 'none'),
    ('a-C', 'Amorphous carbon', 'a-C'),
    ('Ag', 'Silver', 'Ag'),
    ('Al', 'Aluminium', 'Al'),
    ('AlAs', 'Cubic aluminium arsenide', 'AlAs'),
    ('AlAs_palik', 'Cubic aluminium arsenide (p)', 'AlAs_palik'),
    ('AlSb', 'Cubic aluminium antimonide', 'Alsb'),
    ('AlSb_palik', 'Cubic aluminium antimonide (p)', 'AlSb_palik'),
    ('Au', 'Gold', 'Au'),
    ('Be', 'Polycrystalline beryllium', 'Be'),
    ('Be_palik', 'Polycrystalline beryllium (p)', 'Be_palik'),
    ('Cr', 'Chromium', 'Cr'),
    ('CsI', 'Cubic caesium iodide', 'CsI'),
    ('CsI_palik', 'Cubic caesium iodide (p)', 'CsI_palik'),
    ('Cu', 'Copper', 'Cu'),
    ('Cu_palik', 'Copper (p)', 'Cu_palik'),
    ('Cu2O', 'Copper (I) oxide', 'Cu2O'),
    ('Cu2O_palik', 'Copper (I) oxide (p)', 'Cu2O_palik'),
    ('CuO', 'Copper (II) oxide', 'CuO'),
    ('CuO_palik', 'Copper (II) oxide (p)', 'CuO_palik'),
    ('d-C', 'Cubic diamond', 'd-C'),
    ('d-C_palik', 'Cubic diamond (p)', 'd-C_palik'),
    ('Hg', 'Mercury', 'Hg'),
    ('Hg_palik', 'Mercury (p)', 'Hg_palik'),
    ('HgTe', 'Mercury telluride', 'HgTe'),
    ('HgTe_palik', 'Mercury telluride (p)', 'HgTe_palik'),
    ('Ir', 'Iridium', 'Ir'),
    ('Ir_palik', 'Iridium (p)', 'Ir_palik'),
    ('K', 'Polycrystalline potasium', 'K'),
    ('K_palik', 'Polycrystalline potasium (p)', 'K_palik'),
    ('Li', 'Lithium', 'Li'),
    ('Li_palik', 'Lithium (p)', 'Li_palik'),
    ('MgO', 'Magnesium oxide', 'MgO'),
    ('MgO_palik', 'Magnesium oxide (p)', 'MgO_palik'),
    ('Mo', 'Molybdenum', 'Mo'),
    ('Mo_palik', 'Molybdenum (p)', 'Mo_palik'),
    ('Na_palik', 'Sodium (p)', 'Na_palik'),
    ('Nb', 'Niobium', 'Nb'),
    ('Nb_palik', 'Niobium (p)', 'Nb_palik'),
    ('Ni_palik', 'Nickel', 'Ni_palik'),
    ('Rh', 'Rhodium', 'Rh'),
    ('Rh_palik', 'Rhodium (p)', 'Rh_palik'),
    ('Se', 'Selenium', 'Se'),
    ('Se_palik', 'Selenium (p)', 'Se_palik'),
    ('Se-e', 'Selenium (e)', 'Se-e'),
    ('Se-e_palik', 'Selenium (e)(p)', 'Se-e_palik'),
    ('SiC', 'Hexagonal silicon carbide', 'SiC'),
    ('SiC_palik', 'Hexagonal silicon carbide (p)', 'SiC_palik'),
    ('SnTe', 'Tin telluride', 'SnTe'),
    ('SnTe_palik', 'Tin telluride (p)', 'SnTe_palik'),
    ('Ta', 'Tantalum', 'Ta'),
    ('Ta_palik', 'Tantalum (p)', 'Ta_palik'),
    ('Te', 'Trigonal tellurium', 'Te'),
    ('Te_palik', 'Trigonal tellurium (p)', 'Te_palik'),
    ('Te-e', 'Trigonal tellurium (e)', 'Te-e'),
    ('Te-e_palik', 'Trigonal tellurium (e)(p)', 'Te-e_palik'),
    ('ThF4', 'Polycryst. thorium (IV) fluoride', 'ThF4'),
    ('ThF4_palik', 'Polycryst. thorium (IV) fluoride (p)', 'ThF4_palik'),
    ('TiC', 'Polycrystalline titanium carbide', 'TiC'),
    ('TiC_palik', 'Polycrystalline titanium carbide (p)', 'TiC_palik'),
    ('TiN', 'Titanium nitride', 'TiN'),
    ('TiN_palik', 'Titanium nitride (p)', 'TiN_palik'),
    ('TiO2', 'Tetragonal titanium dioxide', 'TiO2'),
    ('TiO2_palik', 'Tetragonal titanium dioxide (p)', 'TiO2_palik'),
    ('TiO2-e', 'Tetragonal titanium dioxide (e)', 'TiO2-e'),
    ('TiO2-e_palik', 'Tetragonal titanium dioxide (e)(p)', 'TiO2-e_palik'),
    ('VC', 'Vanadium carbide', 'VC'),
    ('VC_palik', 'Vanadium carbide (p)', 'VC_palik'),
    ('V_palik', 'Vanadium', 'V_palik'),
    ('VN', 'Vanadium nitride', 'VN'),
    ('VN_palik', 'Vanadium nitride (p)', 'VN_palik'),
    ('W', 'Tungsten', 'W'),
]

medium_material_tree = [
    ("Liquids", [
        ("Skimmilk", 8),
        ("Wholemilk", 12),
        ("Lowfat Milk", 13),
        ("Reduced Milk", 14),
        ("Regular Milk", 15),
        ("Espresso", 16),
        ("Mint Mocha Coffee", 17),
        ("Lowfat Soy Milk", 18),
        ("Regular Soy Milk", 19),
        ("Lowfat Chocolate Milk", 20),
        ("Regular Chocolate Milk", 21),
        ("Coke", 22),
        ("Pepsi", 23),
        ("Sprite", 24),
        ("Gatorade", 25),
        ("Chardonnay", 26),
        ("White Zinfandel", 27),
        ("Merlot", 28),
        ("Budweiser Beer", 29),
        ("Coors Light Beer", 30),
        ("Apple Juice", 32),
        ("Cranberry Juice", 33),
        ("Grape Juice", 34),
        ("Ruby Grapefruit Juice", 35),
        ("White Grapefruit Juice", 36),
        ("Pacific Ocean Surface Water", 47),
    ]),

    ("Powder", [
        ("Lemon Tea Powder", 40),
        ("Orange Juice Powder", 41),
        ("Pink Lemonade Powder", 42),
        ("Cappuccino Powder", 43),
        ("Salt Powder", 44),
        ("Sugar Powder", 45),
        ("Suisse Mocha Powder", 46),
    ]),

    ("Miscellaneous", [
        ("Apple", 1),
        ("Chicken1", 2),
        ("Chicken2", 3),
        ("Cream", 4),
        ("Ketchup", 5),
        ("Marble", 6),
        ("Potato", 7),
        ("Skin1", 9),
        ("Skin2", 10),
        ("Spectralon", 11),
        ("Clorox", 31),
        ("Shampoo", 37),
        ("Strawberry Shampoo", 38),
        ("Head & Shoulders Shampoo", 39),
    ]),
]

medium_material_dict = {
    1: [(2.29, 2.39, 1.97), (0.0030, 0.0034, 0.0460), (0.0, 0.0, 0.0), 1.3],
    2: [(0.15, 0.21, 0.38), (0.0015, 0.0770, 0.1900), (0.0, 0.0, 0.0), 1.3],
    3: [(0.19, 0.25, 0.32), (0.0018, 0.0880, 0.2000), (0.0, 0.0, 0.0), 1.3],
    4: [(7.38, 5.47, 3.15), (0.0002, 0.0028, 0.0163), (0.0, 0.0, 0.0), 1.3],
    5: [(0.18, 0.07, 0.03), (0.0610, 0.9700, 1.4500), (0.0, 0.0, 0.0), 1.3],
    6: [(2.19, 2.62, 3.00), (0.0021, 0.0041, 0.0071), (0.0, 0.0, 0.0), 1.5],
    7: [(0.68, 0.70, 0.55), (0.0024, 0.0090, 0.1200), (0.0, 0.0, 0.0), 1.3],
    8: [(0.70, 1.22, 1.90), (0.0014, 0.0025, 0.0142), (0.0, 0.0, 0.0), 1.3],
    9: [(0.74, 0.88, 1.01), (0.0320, 0.1700, 0.4800), (0.0, 0.0, 0.0), 1.3],
    10: [(1.09, 1.59, 1.79), (0.013, 0.07000, 0.1450), (0.0, 0.0, 0.0), 1.3],
    11: [(11.6, 20.4, 14.9), (0.0000, 0.0000, 0.0000), (0.0, 0.0, 0.0), 1.3],
    12: [(2.55, 3.21, 3.77), (0.0011, 0.0024, 0.0140), (0.0, 0.0, 0.0), 1.3],
    13: [(13.1157, 15.4445, 17.9572), (0.00287, 0.00575, 0.01150), (0.93200, 0.90200, 0.85900), 1.33],
    14: [(13.7335, 15.6003, 17.8007), (0.00256, 0.00511, 0.01278), (0.81900, 0.79700, 0.74600), 1.33],
    15: [(18.2052, 20.3826, 22.3698), (0.00153, 0.00460, 0.01993), (0.75000, 0.71400, 0.68100), 1.33],
    16: [(7.78262, 8.13050, 8.53875), (4.79838, 6.57512, 8.84925), (0.90700, 0.89600, 0.88000), 1.33],
    17: [(3.51133, 4.14383, 5.59667), (3.77200, 5.82283, 7.82000), (0.91000, 0.90700, 0.91400), 1.33],
    18: [(2.03838, 2.32875, 3.90281), (0.00144, 0.00719, 0.03594), (0.85000, 0.85300, 0.84200), 1.33],
    19: [(4.66325, 5.20183, 8.74575), (0.00192, 0.00958, 0.06517), (0.87300, 0.85800, 0.83200), 1.33],
    20: [(9.83710, 11.4954, 13.1629), (0.01150, 0.03680, 0.15640), (0.93400, 0.92700, 0.91600), 1.33],
    21: [(10.5685, 13.1416, 15.2202), (0.01006, 0.04313, 0.14375), (0.86200, 0.83800, 0.80600), 1.33],
    22: [(0.00254, 0.00299, 0.00000), (0.10014, 0.16503, 0.24680), (0.96500, 0.97200, 0.00000), 1.33],
    23: [(0.00083, 0.00203, 0.00000), (0.09164, 0.14158, 0.20729), (0.92600, 0.97900, 0.00000), 1.33],
    24: [(0.00011, 0.00014, 0.00014), (0.00189, 0.00183, 0.00200), (0.94300, 0.95300, 0.95200), 1.33],
    25: [(0.03668, 0.04488, 0.05742), (0.02479, 0.01929, 0.00888), (0.93300, 0.93300, 0.93500), 1.33],
    26: [(0.00021, 0.00033, 0.00048), (0.01078, 0.01186, 0.02400), (0.91400, 0.95800, 0.97500), 1.33],
    27: [(0.00022, 0.00033, 0.00046), (0.01207, 0.01618, 0.01984), (0.91900, 0.94300, 0.97200), 1.33],
    28: [(0.00081, 0.00000, 0.00000), (0.11632, 0.25191, 0.29434), (0.97400, 0.00000, 0.00000), 1.33],
    29: [(0.00029, 0.00055, 0.00059), (0.01149, 0.02491, 0.05779), (0.91700, 0.95600, 0.98200), 1.33],
    30: [(0.00062, 0.00127, 0.00000), (0.00616, 0.01398, 0.03498), (0.91800, 0.96600, 0.00000), 1.33],
    31: [(0.02731, 0.03302, 0.03695), (0.00335, 0.01489, 0.02630), (0.91200, 0.90500, 0.89200), 1.33],
    32: [(0.00257, 0.00311, 0.00413), (0.01296, 0.02374, 0.05218), (0.94700, 0.94900, 0.94500), 1.33],
    33: [(0.00196, 0.00238, 0.00301), (0.03944, 0.09422, 0.12426), (0.94700, 0.95100, 0.97400), 1.33],
    34: [(0.00138, 0.00000, 0.00000), (0.10404, 0.23958, 0.29325), (0.96100, 0.00000, 0.00000), 1.33],
    35: [(0.15496, 0.15391, 0.15995), (0.08587, 0.18314, 0.25262), (0.92900, 0.92900, 0.93100), 1.33],
    36: [(0.50499, 0.52742, 0.75282), (0.01380, 0.01883, 0.05678), (0.54800, 0.54500, 0.56500), 1.33],
    37: [(0.00797, 0.00874, 0.01127), (0.01411, 0.04569, 0.06172), (0.91000, 0.90500, 0.92000), 1.33],
    38: [(0.00215, 0.00245, 0.00253), (0.01449, 0.05796, 0.07582), (0.92700, 0.93500, 0.99400), 1.33],
    39: [(0.26747, 0.27696, 0.29574), (0.08462, 0.15688, 0.20365), (0.91100, 0.89600, 0.88400), 1.33],
    40: [(0.74489, 0.83823, 1.00158), (2.42881, 4.57573, 7.21270), (0.94600, 0.94600, 0.94900), 1.33],
    41: [(0.00193, 0.00213, 0.00226), (0.00145, 0.00344, 0.00786), (0.91900, 0.91800, 0.92200), 1.33],
    42: [(0.00123, 0.00133, 0.00131), (0.00116, 0.00237, 0.00320), (0.90200, 0.90200, 0.90400), 1.33],
    43: [(12.2094, 16.4659, 29.2727), (35.8441, 49.5470, 61.0844), (0.84900, 0.84300, 0.92600), 1.33],
    44: [(0.13805, 0.15677, 0.17865), (0.28415, 0.32570, 0.34148), (0.80200, 0.79300, 0.82100), 1.33],
    45: [(0.00282, 0.00315, 0.00393), (0.01264, 0.03105, 0.05012), (0.92100, 0.91900, 0.93100), 1.33],
    46: [(30.0848, 33.4452, 38.7191), (17.5020, 27.0044, 35.4334), (0.90700, 0.89400, 0.88800), 1.33],
    47: [(0.00180, 0.00183, 0.00228), (0.03184, 0.03132, 0.03015), (0.90200, 0.82500, 0.91400), 1.33],
}