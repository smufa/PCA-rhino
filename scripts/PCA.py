from godot import exposed, export
from godot import *
import numpy as np
from sklearn.decomposition import PCA as PCCA

@exposed
class PCA(MeshInstance):
	
	# member variables here, example:
	# a = export(int)
	# b = export(str, default='foo')
	node_mesh = 0
	node_material = 0
	
	def _ready(self):
		node_mesh = self.get_mesh()
		node_material = self.get_surface_material(0)
		mesh_array = np.array(node_mesh.surface_get_arrays(0)[1]) 
		mesh_array = np.array([np.array([x.x, x.y, x.z]) for x in mesh_array])
		
		pca = PCCA(n_components=2)
		transformed_mesh = pca.fit_transform(mesh_array)
		transform_matrix = pca.components_
		#print(transform_matrix[0])
		#for function in dir(node_material):
		#	if "next_pass" in function:
		#		print(function)
		row1 = transform_matrix[0]
		node_material.set_shader_param("row1", Vector3(row1[0], row1[1], row1[2]))
		row2 = transform_matrix[1]
		node_material.set_shader_param("row2", Vector3(row2[0], row2[1], row2[2]))
