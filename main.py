from numba import njit;

@njit
def calculate_gun_dpc(base_damage, attack_speed, clip_size):
    dps = (base_damage * attack_speed*clip_size)
    return dps

@njit
def calculate_gun_dpm(dps):
    dpm = dps*60
    return dpm

dpc = calculate_gun_dpc(30, 0.2, 54)
dpm = calculate_gun_dpm(dpc)

print(dpm)
print(dpc)