from anuga_bmi import BmiAnuga

cfg = """
domain_type: rectangular
shape: [10, 10]
size: [1.0, 1.0]
output_filename: anuga_output
output_timestep: 10
boundary_conditions: {'left': ['Dirichlet', 0.4, 0, 0],'right': 'Reflective','top': 'Reflective','bottom': 'Reflective'}
elevation_profile : shallow linear ramp
initial_flow_depth: 0.0
toggle_sediment_transport: False
inflow_sediment_concentration: 0.0
initial_sediment_concentration: 0.0
toggle_vegetation_drag: False
vegetation_stem_diameter: 0.0
vegetation_stem_spacing: 0.0
Mannings_n_parameter: 0.0
"""

with open('anuga.yaml', 'w') as fp:
    fp.write(cfg)

model = BmiAnuga()
print model.get_component_name()
model.initialize('anuga.yaml')
model.update()
model.finalize()
