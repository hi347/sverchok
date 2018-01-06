
import unittest
import json

from sverchok.utils.testing import *
from sverchok.utils.sv_IO_panel_tools import create_dict_of_tree

class ScriptUvExportTest(ReferenceTreeTestCase):

    reference_file_name = "script_uv_ref.blend.gz"

    def test_script_uv_export(self):
        export_result = create_dict_of_tree(self.tree)
        self.assert_json_equals_file(export_result, "script_uv.json")

@unittest.skip("Waiting for #2012 to be fixed")
class ProfileExportTest(ReferenceTreeTestCase):

    reference_file_name = "profile_ref.blend.gz"

    def test_profile_export(self):
        export_result = create_dict_of_tree(self.tree)
        self.assert_json_equals_file(export_result, "profile.json")

class MeshExprExportTest(ReferenceTreeTestCase):

    reference_file_name = "mesh_expr_ref.blend.gz"

    def setUp(self):
        # We have to load text block as well
        self.link_text_block("Mesh Expression")
        super().setUp()

    def test_mesh_expr_export(self):
        export_result = create_dict_of_tree(self.tree)
        self.assert_json_equals_file(export_result, "mesh.json")

class MonadExportTest(ReferenceTreeTestCase):

    reference_file_name = "monad_1_ref.blend.gz"

    def setUp(self):
        self.link_node_tree(tree_name="PulledCube")
        super().setUp()

    @unittest.skip("Linking node tree with Monad node does not work correctly.")
    def test_monad_export(self):
        export_result = create_dict_of_tree(self.tree)
        #self.store_reference_json("monad_e.json", export_result)
        self.assert_json_equals_file(export_result, "monad_1.json")

    def tearDown(self):
        remove_node_tree("PulledCube")
        super().tearDown()

