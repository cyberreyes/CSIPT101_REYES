from django.shortcuts import render


def mission(request):
    context = {
        'mission' : 'The college of computer studies shall produce\
            technically competent Information Technology professionals adequately prepared\
                in the practice of their profession supportive of national development goals\
                    and standard of global exellence'
    }
    return render(request, 'Mission.html', context)\
    
def vision(request):
    context = {
        'vision' : 'The College of Computer Studies shall be a\
            center of Excellence in Information Technology education'
    }
    return render(request,'Vision.html', context)

def objectives(request):
    context = {
        'goaltitle' : 'CCMS Program Education Objectives',
        'ccmsgoal' : ' After graduation, alumni of MSEUF-CCS program shall:',
        'one' : '1. Be employed and demonstrate professionalism, competence, and passion in solving contemporary\
            computing problems by developing or utilizing innovative solutions.',
        'two' : '2. Embark in lifelong learning in research to attain to the continuous innovation in the IT industry\
            in order to adapt to the changing demands of the global market.',
        'three' : '3. Exhibit leadership and teamwork, and commitment to their respective local or global organization.',
    }
    return render(request,'Objectives.html', context)

    