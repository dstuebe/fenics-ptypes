#!/usr/bin/env python

"""
@package
@file fenics-ptypes/tag.py
@author Christopher Mueller
@author David Stuebe
@brief Tag object similar to MOAB for fenics mesh and mesh functions
"""

from dolfin import MeshFunction, Mesh
import numpy

def ion_ehandle(entity):
    return entity.dim(), entity.index()


class IonTag(object):

    def __init__(self, name, size, type, mesh):

        self._name = name
        self._size = size
        self._type = type
        self._mesh = mesh

        #@todo - can we pass/use a memory mapped object?
        self._value_func = lambda x: numpy.fromiter(x, dtype=self._type, count=self._size)

        self._entity_values={}

    def __getitem__(self, entity):
        return self._entity_values[ion_ehandle(entity)]


    def __setitem__(self, entity, values):
        assert entity.mesh() is self._mesh, 'Do not put entities from different meshes in the same tag!'
        self._entity_values[ion_ehandle(entity)] = self._value_func(values)

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __contains__(self, k): # real signature unknown; restored from __doc__
        """ D.__contains__(k) -> True if D has a key k, else False """
        return False

    def iteritems(self): # real signature unknown; restored from __doc__
        """ D.iteritems() -> an iterator over the (key, value) items of D """
        for k, v in self._entity_values.iteritems():
            #@todo - how do we get the entity back rather than our handle???
            yield k, v


    def iterkeys(self): # real signature unknown; restored from __doc__
        """ D.iterkeys() -> an iterator over the keys of D """
        pass

    def itervalues(self): # real signature unknown; restored from __doc__
        """ D.itervalues() -> an iterator over the values of D """
        pass
