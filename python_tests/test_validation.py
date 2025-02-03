from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance


import yaml



with open('../yaml/test.yaml', 'r') as yam:
    prog = yaml.safe_load(yam)



MODEL_REGISTRY = {'QuadScanEmittance': QuadScanEmittance}

for k, v in prog.items():
    if k in MODEL_REGISTRY:
        p = MODEL_REGISTRY[k].model_validate(v)


print(type(p))
print(p.scan_values)