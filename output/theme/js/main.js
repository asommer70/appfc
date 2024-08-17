function parseICS(icsString) { 
        //console.log('icsString:', icsString);
        const lines = icsString.split('\n'); 
        const events = []; 
        let event; 
        for (let i = 0; i < lines.length; i++) { 
                const line = lines[i].trim(); 
                if (line === 'BEGIN:VEVENT') { 
                        event = {}; 
                } else if (line === 'END:VEVENT') { 
                        events.push(event); 
                } else if (event) { 
                        const match = /^([A-Z]+):(.*)$/.exec(line); 
                        if (match) { 
                                const [, key, value] = match; event[key] = value; 
                        } 
                } 
        }
        console.log('events[0]:', events[0])
        return events; 
}

async function getICS() {
  const response = await fetch('/theme/data/lander_2024.ics');
  return await response.text();
}

console.log('ready.......................');
//const landerCal = getICS();
//console.log('landerCal:', landerCal);
getICS().then((res) => parseICS(res));
//const landerEvents = parseICS(landerCal);
//console.log('landerEvents: ', landerEvents); 

