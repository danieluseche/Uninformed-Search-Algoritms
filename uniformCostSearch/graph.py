import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

if __name__=='__main__':

    with open('output.time') as f:
        text = f.read()

    cities = []
    time = []
    time_in_seconds =[]

    for line in text.splitlines():
        if line.startswith('Problem'):
            cities.append(int(line.split(' ')[1].strip('gr')))

        if line.startswith('real'):
            time.append(line.split('\t')[1].split('m'))

    
    for t in time: 
        time_in_seconds.append(int(t[0]) * 60 + float(t[1].replace(',','.').strip('s')))
    

    plt.style.use('_mpl-gallery')

    # plot
    
    plt.xlabel('N° Cities')
    plt.ylabel('Seconds to solve')
    plt.title('TSP complexity with uniform cost search')
    plt.plot(cities, time_in_seconds, '-o', linewidth=2.0)
    plt.savefig('TSP_complexity_Plot.svg', bbox_inches='tight')
