"""Auxiliary functions used in several notebooks of the repo."""

import numpy as np

# Geophysical parameter: Earth radius
Earth_radius = 6370e3     # in meters

def set_boundaries_to_zero(field):
    f = np.copy(field)
    f[0,:]  = f[-1,:] = f[:,0]  = f[:,-1] = 0
    return f

def von_neuman_euler(field, axis=None):
    """Apply Von Neuman boundary conditions to the field."""
    f = np.copy(field)
    if axis == 0 or None:
        f[0,:]  = f[1,:]
        f[-1,:] = f[-2,:]
    if axis == 1 or None:
        f[:,0]  = f[:,1]
        f[:,-1] = f[:,-2]
    return f

def derivative(field, lon, lat, axis):
    """Compute partial derivative using second-order centered scheme.
    field: field to derive
    lon, lat: longitude and latitude arrays, same size as field
    axis: along which derivation is carried out.
    axis = 0 corresponds to latitude, axis = 1 corresponds to longitude.
    The output is in field_unit/meters.
    """
    f = 0.5 * ( np.roll(field, -1, axis=axis) - np.roll(field, 1, axis=axis) )
    if axis == 0:
        dx = 0.5 * ( np.roll(lat, -1, axis=0) - np.roll(lat, 1, axis=0) ) * np.pi / 180     # in radian
        dx = dx * Earth_radius
    if axis == 1:
        dx = 0.5 * ( np.roll(lon, -1, axis=1) - np.roll(lon, 1, axis=1) ) * np.pi / 180     # in radian
        dx = dx * Earth_radius * np.cos(lat*np.pi/180)
    f = f / dx
    f = von_neuman_euler(f, axis=axis)
    return f

def gradient(field, lon, lat):
    """Compute gradient of input scalar field."""
    fx, fy = derivative(field, lon, lat, axis=1), derivative(field, lon, lat, axis=0)
    return fx, fy

def divergence(u, v, lon, lat):
    """Compute divergence of a 2D-vector with components u, v."""
    f = derivative(u, lon, lat, axis=1) + derivative(v, lon, lat, axis=0)
    return f

def rotational(u, v, lon, lat):
    """Compute vertical component of rotational of a 2D-vector with components u, v."""
    f = derivative(v, lon, lat, axis=1) - derivative(u, lon, lat, axis=0)
    return f

def laplacian(field):
    """Compute Laplacian of field."""
    fx = np.roll(field, -1, axis=0) -2 * field + np.roll(field, 1, axis=0)
    fy = np.roll(field, -1, axis=1) -2 * field + np.roll(field, 1, axis=1)
    f = fx + fy
    f = von_neuman_euler(f)
    return f

def advection(u, v, lon, lat):
    u2, v2, uv = u*u, v*v, u*v
    adv_u = derivative(u2, lon, lat, axis=1) + derivative(uv, lon, lat, axis=0) #- divergence(u,v,lon,lat)
    adv_v = derivative(uv, lon, lat, axis=1) + derivative(v2, lon, lat, axis=0) #- divergence(u,v,lon,lat)
    return adv_u, adv_v