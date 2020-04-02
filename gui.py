#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = Tk()

WINDOW_HEIGHT = 700
WINDOW_WIDTH  = 1200

image_files = [Image.open('Projection Photolithography.png'),
               Image.open('Proximity Photolithography.png'),
               Image.open('Electron Beam Lithography.png'),
               Image.open('Focused Ion Beam Writing.png'),
               Image.open('Proton Beam Writing.png'),
               Image.open('Ion Projection Lithography.png')]
image_files[0] = image_files[0].resize((int(986.0/640 * WINDOW_HEIGHT/3.2), int(WINDOW_HEIGHT/3.2)), Image.ANTIALIAS) 
image_files[1] = image_files[1].resize((int(1279.0/467 * WINDOW_HEIGHT/6.4), int(WINDOW_HEIGHT/6.4)), Image.ANTIALIAS) 
image_files[2] = image_files[2].resize((int(677.0/455 * WINDOW_HEIGHT/3.2), int(WINDOW_HEIGHT/3.2)), Image.ANTIALIAS) 
image_files[3] = image_files[3].resize((int(651.0/694 * WINDOW_HEIGHT/3.2), int(WINDOW_HEIGHT/3.2)), Image.ANTIALIAS) 
image_files[4] = image_files[4].resize((int(895.0/630 * WINDOW_HEIGHT/3.2), int(WINDOW_HEIGHT/3.2)), Image.ANTIALIAS) 
image_files[5] = image_files[5].resize((int(816.0/633 * WINDOW_HEIGHT/3.2), int(WINDOW_HEIGHT/3.2)), Image.ANTIALIAS) 

image_tks = [ImageTk.PhotoImage(image_files[0]),
             ImageTk.PhotoImage(image_files[1]),
             ImageTk.PhotoImage(image_files[2]),
             ImageTk.PhotoImage(image_files[3]),
             ImageTk.PhotoImage(image_files[4]),
             ImageTk.PhotoImage(image_files[5])]

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

def getBlurb(process):
    blurb = ''

    if process == 'Projection Photolithography':
        blurb = 'Projection photolithography transfers a pattern from a mask that has the desired pattern onto a photo-sensitive substrate. The light passes through the mask and is then focused through a series of lenses before reaching the substrate. This allows for the pattern projected onto the substrate to be many times smaller than the pattern on the photo mask. It has a high throughput due to its parallel nature (the entire pattern is printed at once) but is limited to use on photo-sensitive materials.'

    elif process == 'Proximity Photolithography':
        blurb = 'Proximity photolithography uses lightto transfer a pattern from a mask that has the desired pattern onto a photo-sensitive substrate. The light passes through the mask and then hits the photo-sensitive substrate. It has a high throughput due to its parallel nature (the entire pattern is printed at once) but is limited to use on photo-sensitive materials.'
        
    elif process == 'Electron Beam Lithography':
        blurb = 'Electron Beam Lithography uses a focused beam of electrons and an electron-sensitive resist to produce 2D etching. Extremely low resolutions can be achieved when compared to masked processes, but due to electron scattering, resolution generally peaks at around 50nm. Since it is a single-beam writing process, no 3D structures can be achieved, and the throughput is very low. Machine costs are also very high, but an electron microscope can be retrofitted to become an e-Beam lithography machine to reduce costs. As a result, e-Beam is generally reserved for low volume fabrication or research.'
        
    elif process == 'Focused Ion Beam Writing':
        blurb = 'Focused ion beam writing uses a focused beam of slower heavy ions (with energy around 30keV) to induce a sputtering material removal effect on the substrate. Due to the sputtering material interaction, it is not restricted to resist materials. Complex 3D structures are also possible thanks to limited proximity effects of secondary electrons.'
        
    elif process == 'Proton Beam Writing':
        blurb = 'Proton beam writing (p-beam) uses a focused beam of high energy ions (typically with energy around 1-2 MeV) to penetrate the resist material. 3D structures with high aspect ratios are possible thanks to this high penetration and minimal proximity effects. Depth of penetration can be controlled precisely with ion energy.'
        
    elif process == 'Ion Projection Lithography':
        blurb = 'Ion projection lithography (IPL) uses the advantages of ion beam writing, namely minimal diffraction and proximity effects, as well as the advantages of a masked process, writing an entire layer at once. Due to this, higher throughputs can be achieved while still maintaining <100nm resolutions.'

    return blurb


def getImage(process):
    if process == 'Projection Photolithography':
        return image_tks[0]

    elif process == 'Proximity Photolithography':
        return image_tks[1]
        
    elif process == 'Electron Beam Lithography':
        return image_tks[2]
        
    elif process == 'Focused Ion Beam Writing':
        return image_tks[3]
        
    elif process == 'Proton Beam Writing':
        return image_tks[4]
        
    elif process == 'Ion Projection Lithography':
        return image_tks[5]


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


def main():
    # Initialization
    window.title('Nanofab Process Selection')
    window.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))
    window.resizable(width=False, height=False)

    myfont = ('Arial', 12)
    myfont_bold = ('Arial', 12, 'bold')

    # Intro text
    intro_text_1 = Label(window, text='Welcome to the nano-fabrication process selection tool.', font=myfont_bold)
    intro_text_2 = Label(window,
                         text='This tool will guide you through process selection by allowing you to specify your process parameters. The tool will then choose the best manufacturing method(s) for',
                         font=myfont)
    intro_text_3 = Label(window,
                         text='your purposes based on the information you have provided. Use the below interface to set your process parameters and then click the \"Confirm\" button.',
                         font=myfont)

    intro_text_1.grid(column=0, row=0, columnspan=5, rowspan=1, pady='10')
    intro_text_2.grid(column=0, row=1, sticky='NW', columnspan=5, rowspan=1)
    intro_text_3.grid(column=0, row=2, sticky='NW', columnspan=5, rowspan=1)

    intro_separator = Canvas(window, width=WINDOW_WIDTH, height=25)
    intro_separator.create_line(50, 12, WINDOW_WIDTH-50, 12, fill="grey")
    intro_separator.grid(column=0, row=4, columnspan=5, rowspan=1)

    # Slider
    res_var = IntVar()
    res_scale = Scale(window, variable=res_var, orient=HORIZONTAL, from_=5, to=2000, font=myfont, length=350, label='Required resolution (nm):')
    res_scale.grid(column=0, row=5, columnspan=2, rowspan=4)

    row1_separator = Canvas(window, width=30, height=100)
    row1_separator.create_line(15, 32, 15, 85, fill="grey")
    row1_separator.grid(column=2, row=5, columnspan=1, rowspan=4)

    # Material properties checkboxes
    mats_label = Label(window, text='Properties of the materials (check all that apply):', font=myfont)
    mats_label.grid(column=3, row=5, columnspan=2, rowspan=1, sticky='W')

    mats_var = [BooleanVar(), BooleanVar(), BooleanVar()]

    for mat in mats_var:
        mat.set(False)

    mats_checkboxes = [Checkbutton(window, text='Photosensitive',     var=mats_var[0], font=myfont),
                       Checkbutton(window, text='Electron-sensitive', var=mats_var[1], font=myfont),
                       Checkbutton(window, text='Resist',             var=mats_var[2], font=myfont)]

    mats_checkboxes[0].grid(column=3, row=6, columnspan=2, rowspan=1, sticky='W')
    mats_checkboxes[1].grid(column=3, row=7, columnspan=2, rowspan=1, sticky='W')
    mats_checkboxes[2].grid(column=3, row=8, columnspan=2, rowspan=1, sticky='W')

    # Geometry selection
    geometry_label = Label(window, text='Geometry of the fabricated structure:', font=myfont)
    geometry_label.grid(column=0, row=9, columnspan=1, rowspan=1, sticky='W')

    geometry_var = IntVar()

    geometry_choices = [Radiobutton(window, text='2D', value=1, variable=geometry_var, font=myfont),
                        Radiobutton(window, text='3D', value=2, variable=geometry_var, font=myfont),
                        Radiobutton(window, text='3D (with high aspect ratios)', value=3, variable=geometry_var, font=myfont)]

    geometry_choices[0].grid(column=0, row=10, columnspan=1, rowspan=1, sticky='W')
    geometry_choices[1].grid(column=0, row=11, columnspan=1, rowspan=1, sticky='W')
    geometry_choices[2].grid(column=0, row=12, columnspan=1, rowspan=1, sticky='W')
    geometry_choices[0].select()

    row2_separator1 = Canvas(window, width=30, height=100)
    row2_separator1.create_line(15, 32, 15, 85, fill="grey")
    row2_separator1.grid(column=1, row=9, columnspan=1, rowspan=4)

    # Throughput selection
    throughput_label = Label(window, text='Required throughput:', font=myfont)
    throughput_label.grid(column=2, row=9, columnspan=1, rowspan=1, sticky='W')

    throughput_var = IntVar()

    thoughtput_choices = [Radiobutton(window, text='Low', value=1, variable=throughput_var, font=myfont),
                          Radiobutton(window, text='Medium', value=2, variable=throughput_var, font=myfont),
                          Radiobutton(window, text='High', value=3, variable=throughput_var, font=myfont)]

    thoughtput_choices[0].grid(column=2, row=10, columnspan=1, rowspan=1, sticky='W')
    thoughtput_choices[1].grid(column=2, row=11, columnspan=1, rowspan=1, sticky='W')
    thoughtput_choices[2].grid(column=2, row=12, columnspan=1, rowspan=1, sticky='W')
    thoughtput_choices[0].select()

    row2_separator2 = Canvas(window, width=30, height=100)
    row2_separator2.create_line(15, 32, 15, 85, fill="grey")
    row2_separator2.grid(column=3, row=9, columnspan=1, rowspan=4)

    # Cost selection
    cost_label = Label(window, text='Allowable equipment cost:', font=myfont)
    cost_label.grid(column=4, row=9, columnspan=1, rowspan=1, sticky='W')

    cost_var = IntVar()

    cost_choices = [Radiobutton(window, text='Low', value=1, variable=cost_var, font=myfont),
                          Radiobutton(window, text='Medium', value=2, variable=cost_var, font=myfont),
                          Radiobutton(window, text='High', value=3, variable=cost_var, font=myfont)]

    cost_choices[0].grid(column=4, row=10, columnspan=1, rowspan=1, sticky='W')
    cost_choices[1].grid(column=4, row=11, columnspan=1, rowspan=1, sticky='W')
    cost_choices[2].grid(column=4, row=12, columnspan=1, rowspan=1, sticky='W')
    cost_choices[0].select()

    # Notebook
    tab_control = ttk.Notebook(window, width=WINDOW_WIDTH)
    tabs = []
    the_following_label = Label(window, text='The following nano-scale manufacturing methods suit your provided process parameters:\n', font=myfont_bold, justify=LEFT)
    none_label = Label(window, text='Based on your provided parameters, none of this tool\'s supported manufacturing processes suit your fabrication needs.\n\nTry compromising on some process parameters, such as resolution, equipment cost, or required throughput.', font=myfont_bold, justify=LEFT)

    def confirm():
        resolution = res_var.get()

        material_properties = []
        if mats_var[0].get():
            material_properties.append('Photosensitive')
        if mats_var[1].get():
            material_properties.append('Electron-sensitive')
        if mats_var[2].get():
            material_properties.append('Resist')

        geometry = '2D'
        if geometry_var.get() == 1:
            geometry = '2D'
        elif geometry_var.get() == 2:
            geometry = '3D'
        elif geometry_var.get() == 3:
            geometry = '3D (with high aspect ratios)'

        throughput = 'Low'
        if throughput_var.get() == 1:
            throughput = 'Low'
        elif throughput_var.get() == 2:
            throughput = 'Medium'
        elif throughput_var.get() == 3:
            throughput = 'High'

        cost = 'Low'
        if cost_var.get() == 1:
            cost = 'Low'
        elif cost_var.get() == 2:
            cost = 'Medium'
        elif cost_var.get() == 3:
            cost = 'High'

        methods = checkParams(resolution, material_properties, geometry, throughput, cost)

        for tab in tabs:
            tab_control.forget(tab)

        tabs.clear()

        for process in methods:
            tab = ttk.Frame(tab_control)
            tabs.append(tab)
            tab_control.add(tab, text=process)

            blurb = Label(tab, text=getBlurb(process), font=myfont, justify=LEFT, wraplength=int(WINDOW_WIDTH/2), width=70)
            blurb.grid(column=0, row=0, columnspan=1, rowspan=1, sticky='NW', pady=10)

            image_canvas = Canvas(tab, width=WINDOW_WIDTH/3.2, height=WINDOW_HEIGHT/3.2)
            image_canvas.create_image(WINDOW_WIDTH/6.4, WINDOW_HEIGHT/6.4, image=getImage(process))
            image_canvas.grid(column=1, row=0, columnspan=1, rowspan=1)


        # if processes empty



        if (methods):
            none_label.grid_forget()
            the_following_label.grid(column=0, row=14, columnspan=8, rowspan=1, sticky='W')
            tab_control.grid(column=0, row=15, columnspan=8, sticky='W')
        else:
            the_following_label.grid_forget()
            tab_control.grid_forget()
            none_label.grid(column=0, row=14, columnspan=8, rowspan=1, sticky='W')


    # Confirm button
    confirm_button = Button(window, text="Confirm", font=myfont, command=confirm)
    confirm_button.grid(column=2, row=13, pady=10)


    mainloop()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('')
        window.destroy()
