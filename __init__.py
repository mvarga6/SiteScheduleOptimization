# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SiteScheduleOptimization
                                 A QGIS plugin
 Finds an optimal multi-day schedule for traveling to a set of locations.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-08-09
        copyright            : (C) 2022 by Mike Varga
        email                : mvarga6@kent.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SiteScheduleOptimization class from file SiteScheduleOptimization.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .site_schedule_optimization import SiteScheduleOptimization

    return SiteScheduleOptimization(iface)
