### Utilities ###
import maya.cmds as cmds
import re
import sys

#import baseTools as bt#
#toolUtil = bt.tools()#

class tools:
	def __init__(self, sel):
		self.sel = sel

	def searchRE(self, search_parameter, sel):
		search_out = re.search(search_parameter, sel)
		if search_out:
			return search_out
		else:
			cmds.error("Please check search parameter and sel : parameter = what's being searched, sel = where are we searching")

	def typeObject(self, object, type):
		if isinstance(object, type) == True : return True
		else : return False

	def seg_hierachy(self, seg):
		main = cmds.createNode("transform", name = seg + "_GRP")
		skel = cmds.createNode("transform", name = seg + "_SKEL")
		ctrl = cmds.createNode("transform", name = seg + "_CTRL")
		parts = cmds.createNode("transform", name = seg + "_PARTS")

		skelGEO = cmds.duplicate(self.sel[0])
		cmds.select(cl = True)

		cmds.parent(skelGEO[0], skel)
		cmds.parent([skel, ctrl, parts], main)

	def snap(self):
		pc = cmds.pointConstraint(self.source_target_list[0], self.source_target_list[1])
		cmds.delete(pc)

		oc = cmds.orientConstraint(self.source_target_list[0], self.source_target_list[1])
		cmds.delete(oc)

	def blendshapeSet(self):
		cmds.blendshape(self.source_target_list[0], self.source_target_list[1], weight = [(0,1)])