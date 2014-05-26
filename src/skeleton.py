from visual import *
import math

class Bone:
    
    def __init__(self, child, parent):
        self.child = child
        self.parent = parent
        self.child.position_changed = self.update
        self.parent.position_changed = self.update
        self.fixed_size = self.bonesize()
        
    def bonesize(self):
        return math.sqrt((self.parent.x - self.child.x)**2 +
                         (self.parent.y - self.child.y)**2 +
                         (self.parent.z - self.child.z)**2)
    
    def update(self):
        if self.bonesize() != self.fixed_size:
            pass
    
class Joint:
    
    def __init__(self, x, y, z, parent):
        self._x = x
        self._y = y
        self._z = z
        self.parent = parent
        
        if self.parent is not None:
            self._x += parent.x
            self._y += parent.y
            self._z += parent.z
            self.parent = parent
            self.parent.update = self.parent_changed
            
            self.bone = self.create_bone()
        else:
            self.bone = None
        
    def create_bone(self):
        return Bone(self, self.parent)
            
    def update_bone_to_parent(self):
        pass
    
    def parent_changed(self):
        self.update_bone_to_parent()
    
    def child_changed(self, child):
        pass
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self.x = value
        self.update()
    
    @property 
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self.y = value
        self.update()
    
    @property 
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value):
        self.z = value 
        self.update()
    
    #@parent.setter
    #def parent(self, value):
    #    self.parent = value
    #    self.notify_parent()

class VisualBone(Bone):
    
    def __init__(self, child, parent):
        Bone.__init__(self, child, parent)
        self.obj = cylinder(radius=0.15, color=color.orange)
        self.update()
        
    def update(self):
        self.obj.pos = (self.child.x, self.child.y, self.child.z)
        self.obj.axis = (self.parent.x - self.child.x, self.parent.y - self.child.y, self.parent.z - self.child.z)
        
    def draw(self):
        pass
    
class VisualJoint(Joint):
    
    def __init__(self, x, y, z, parent, lbl="", radius=0.3):
        Joint.__init__(self, x, y, z, parent)
        self.obj = sphere(pos=(self.x, self.y, self.z), radius=radius, color=color.orange)
        self._label = None

    def create_label(self, text, xoffset=0, yoffset=0):
        self.label = label(pos=self.obj.pos,
                           text=str(self.obj.pos),
                           xoffset=xoffset,
                           yoffset=yoffset)
        
    def create_bone(self):
        return VisualBone(self, self.parent)
        
    def draw(self):
        pass

class Spine(VisualJoint):

    def __init__(self):
        VisualJoint.__init__(self, 0, 0, 0, None)
        self.create_label("Spine", -80, 70)
        
class Head(VisualJoint):

    def __init__(self, cshoulder):
        VisualJoint.__init__(self, 0, 1, 0.4, cshoulder)
        self.create_label("Head", yoffset=70)
        self.obj.radius = 0.4

class CentralShoulder(VisualJoint):

    def __init__(self, spine):
        VisualJoint.__init__(self, 0, 0.8, -0.2, spine)
        self.create_label("Central shoulder", -70, 70)

class RightShoulder(VisualJoint):

    def __init__(self, cshoulder):
        VisualJoint.__init__(self, -1, 0, 0.2, cshoulder)
        self.create_label("Right shoulder", -40)

class RightElbow(VisualJoint):

    def __init__(self, rshoulder):
        VisualJoint.__init__(self, 0, -1.4, 0, rshoulder)
        self.create_label("Right elbow", -40, 10)

class RightWrist(VisualJoint):

    def __init__(self, relbow):
        VisualJoint.__init__(self, 0, -1.6, 0, relbow)
        self.create_label("Right wrist", -40, -10)

class LeftShoulder(VisualJoint):
    
    def __init__(self, cshoulder):
        VisualJoint.__init__(self, 1, 0, 0.2, cshoulder)
        self.create_label("Left shoulder", 40)

class LeftElbow(VisualJoint):

    def __init__(self, lshoulder):
        VisualJoint.__init__(self, 0, -1.4, 0, lshoulder)
        self.create_label("Left elbow", 40, 10)

class LeftWrist(VisualJoint):

    def __init__(self, lwrist):
        VisualJoint.__init__(self, 0, -1.6, 0, lwrist)
        self.create_label("Left wrist", 40, -10)

class Pelvis(VisualJoint):

    def __init__(self, spine):
        VisualJoint.__init__(self, 0, -1, 0.3, spine)
        self.create_label("Pelvis", 40, 120)

class RightHip(VisualJoint):

    def __init__(self, pelvis):
        VisualJoint.__init__(self, -0.5, -0.3, -0.1, pelvis)
        self.create_label("Right hip", -40)

class RightKnee(VisualJoint):

    def __init__(self, rhip):
        VisualJoint.__init__(self, 0, -2, 0, rhip)
        self.create_label("Right knee", -40, -10)

class RightAnkle(VisualJoint):

    def __init__(self, rknee):
        VisualJoint.__init__(self, 0, -2, 0, rknee)
        self.create_label("Right ankle", -40, 10)

class LeftHip(VisualJoint):

    def __init__(self, pelvis):
        VisualJoint.__init__(self, 0.5, -0.3, -0.1, pelvis)
        self.create_label("Left hip", 40)

class LeftKnee(VisualJoint):

    def __init__(self, lhip):
        VisualJoint.__init__(self, 0, -2, 0, lhip)
        self.create_label("Left knee", 40, -10)

class LeftAnkle(VisualJoint):

    def __init__(self, lknee):
        VisualJoint.__init__(self, 0, -2, 0, lknee)
        self.create_label("Left ankle", 40, 10)
        
class Skeleton(object):
    
    def __init__(self):
        self.spine = Spine()
        self.cshoulder = CentralShoulder(self.spine)
        self.head = Head(self.cshoulder)
        
        self.rshoulder = RightShoulder(self.cshoulder)
        self.relbow = RightElbow(self.rshoulder)
        self.rwrist = RightWrist(self.relbow)

        self.lshoulder = LeftShoulder(self.cshoulder)
        self.lelbow = LeftElbow(self.lshoulder)
        self.lwrist = LeftWrist(self.lelbow)
        
        self.pelvis = Pelvis(self.spine)

        self.rhip = RightHip(self.pelvis)
        self.rknee = RightKnee(self.rhip)
        self.rankle = RightAnkle(self.rknee)

        self.lhip = LeftHip(self.pelvis)
        self.lknee = LeftKnee(self.lhip)
        self.lankle = LeftAnkle(self.lknee)

if __name__ == '__main__':
    s = Skeleton()    
    
