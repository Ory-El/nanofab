#!/usr/bin/env python

import inquirer
import re

processes = {
    'Projection Photolithography' : {
        'Typically attainable resolution (nm)' : 7,
        'Material properties' : ['Photosensitive'],
        'Geometries': ['2D'],
        'Throughput': 3,
        'Equipment cost': 3
    },

    'Proximity Photolithography' : {
        'Typically attainable resolution (nm)' : 2000,
        'Material properties' : ['Photosensitive'],
        'Geometries': ['2D'],
        'Throughput': 3,
        'Equipment cost': 1
    },

    'Electron Beam Lithography' : {
        'Typically attainable resolution (nm)' : 50,
        'Material properties' : ['Electron-sensitive'],
        'Geometries': ['2D'],
        'Throughput': 1,
        'Equipment cost': 2
    },

    'Focused Ion Beam Writing' : {
        'Typically attainable resolution (nm)' : 30,
        'Material properties' : ['Unrestricted'],
        'Geometries': ['2D', '3D', '3D (with high aspect ratios)'],
        'Throughput': 1,
        'Equipment cost': 2
    },

    'Proton Beam Writing' : {
        'Typically attainable resolution (nm)' : 30,
        'Material properties' : ['Resist'],
        'Geometries': ['2D', '3D', '3D (with high aspect ratios)'],
        'Throughput': 2,
        'Equipment cost': 2
    },

    'Ion Projection Lithography' : {
        'Typically attainable resolution (nm)' : 75,
        'Material properties' : ['Resist'],
        'Geometries': ['2D', '3D'],
        'Throughput': 3,
        'Equipment cost': 3
    }
}

lmh_dict = {
    'Low': 1,
    'Medium': 2,
    'High': 3
}

def checkResolution(res, check_procs):
    res_val = float(res)
    return [proc for proc in check_procs if res_val >= processes[proc]['Typically attainable resolution (nm)']]


def checkMaterials(mat_props, check_procs):
    mat_props_app = mat_props + ['Unrestricted']
    return [proc for proc in check_procs for property in mat_props_app if property in processes[proc]['Material properties']]


def checkGeometry(geo, check_procs):
    return [proc for proc in check_procs if geo in processes[proc]['Geometries']]


def checkThroughput(thp, check_procs):
    thp_val = lmh_dict[thp]
    return [proc for proc in check_procs if thp_val <= processes[proc]['Throughput']]


def checkCost(cost, check_procs):
    cost_val = lmh_dict[cost]
    return [proc for proc in check_procs if cost_val >= processes[proc]['Equipment cost']]


def checkParams(resolution, material_properties, geometry, throughput, equipment_cost):
    available_processes = [x for x in processes]

    available_processes = checkResolution(resolution, available_processes)
    available_processes = checkMaterials(material_properties, available_processes)
    available_processes = checkGeometry(geometry, available_processes)
    available_processes = checkThroughput(throughput, available_processes)
    available_processes = checkCost(equipment_cost, available_processes)

    return available_processes


def getInputs():
    questions = [
        inquirer.Text('resolution',
                      message = 'Required resolution (nm)',
                      validate = lambda _, x: re.fullmatch(r'[+-]?((\d+\.?\d*)|(\d*\.?\d+))', x)),

        inquirer.Checkbox('material_properties',
                          message = 'Properties of the materials (check all that apply)',
                          choices = ['Photosensitive', 'Electron-sensitive', 'Resist']),

        inquirer.List('geometry',
                      message = 'Geometry of the fabricated structure',
                      choices = ['2D', '3D', '3D (with high aspect ratios)']),

        inquirer.List('throughput',
                      message = 'Required throughput of the process',
                      choices = ['Low', 'Medium', 'High']),

        inquirer.List('equipment_cost',
                      message = 'Allowable cost of the equipment',
                      choices = ['Low', 'Medium', 'High'])
    ]

    answers = inquirer.prompt(questions)
    return answers


def main():
    print('Welcome to the nano-fabrication process selection tool.',
          '\n\nThis tool will guide you through the selection process by asking questions about your\nmanufacturing requirements.',
          'The tool will then select the best process for your purposes\nbased on the information you have provided.\n')

    while True:
        input('Press enter to continue.')
        print('')

        params = getInputs()

        successful_processes = checkParams(params['resolution'],
                                           params['material_properties'],
                                           params['geometry'],
                                           params['throughput'],
                                           params['equipment_cost'])

        if not successful_processes:
            print('Based on your provided parameters, none of this tool\'s supported manufacturing processes\nsuit your nanoscale fabrication needs.',
                  'Try compromising on some process parameters, such as\nequipment cost or required throughput.')
        else:
            print('Based on your provided parameters, the following manufacturing processes\nsuit your nanoscale fabrication needs:')
            print(successful_processes)

        print('\nRestarting tool.')


if __name__ == "__main__":
    main()