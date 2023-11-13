let map;

// Define setStyle function
function setStyle(params) {
  const datasetFeature = params.feature;
  const assault = parseFloat(datasetFeature.datasetAttributes["AssaultOffense"]); 
  const homicide = parseFloat(datasetFeature.datasetAttributes["Homicide"]); 
  const burglary = parseFloat(datasetFeature.datasetAttributes["Burglary"]); 
  const criminaldamage = parseFloat(datasetFeature.datasetAttributes["CriminalDamage"]); 
  const robbery = parseFloat(datasetFeature.datasetAttributes["Robbery"]); 
  const sexoffense = parseFloat(datasetFeature.datasetAttributes["SexOffense"]); 
  const theft = parseFloat(datasetFeature.datasetAttributes["Theft"]); 
  const vehicletheft = parseFloat(datasetFeature.datasetAttributes["VehicleTheft"]); 
  const arson = parseFloat(datasetFeature.datasetAttributes["Arson"]); 

  console.log("AssaultOffense:", assault);
  console.log("Homicide:", homicide);
  console.log("Burglary:", burglary);
  console.log("CriminalDamage:", criminaldamage);
  console.log("Robbery:", robbery);
  console.log("SexOffense:", sexoffense);
  console.log("Theft:", theft);
  console.log("VehicleTheft:", vehicletheft);
  console.log("Arson:", arson);

  switch (true) {
    case !isNaN(assault) && assault === 1:
      console.log("Setting style for AssaultOffense");
      return { fillColor: "#00008b", strokeColor: "#00008b", pointRadius: 8 }; 
    case !isNaN(homicide) && homicide === 1:
      console.log("Setting style for Homicide");
      return { fillColor: "#8b0000", strokeColor: "#8b0000", pointRadius: 8 }; 
    case !isNaN(burglary) && burglary === 1:
      console.log("Setting style for Burglary");
      return { fillColor: "#FBBC04", strokeColor: "#FBBC04", pointRadius: 8 }; 
    case !isNaN(criminaldamage) && criminaldamage === 1:
      console.log("Setting style for CriminalDamage");
      return { fillColor: "#34A853", strokeColor: "#34A853", pointRadius: 8 };
    case !isNaN(robbery) && robbery === 1:
      console.log("Setting style for Robbery");
      return { fillColor: "#905922", strokeColor: "#905922", pointRadius: 8 }; 
    case !isNaN(sexoffense) && sexoffense === 1:
      console.log("Setting style for SexOffense");
      return { fillColor: "#000000", strokeColor: "#000000", pointRadius: 8 }; 
    case !isNaN(theft) && theft === 1:
      console.log("Setting style for Theft");
      return { fillColor: "#808000", strokeColor: "#808000", pointRadius: 8 }; 
    case !isNaN(vehicletheft) && vehicletheft === 1:
      console.log("Setting style for VehicleTheft");
      return { fillColor: "#542f3f", strokeColor: "#542f3f", pointRadius: 8 }; 
    case !isNaN(arson) && arson === 1:
      console.log("Setting style for Arson");
      return { fillColor: "#ffa500", strokeColor: "#ffa500", pointRadius: 8 }; 
    // default:
    //   console.log("Setting default style");
    //   return { fillColor: "#808080", pointRadius: 8 }; 
  }
}

function makeLegend(map) {
  let colors = {
    "AssaultOffense": ["#00008b"],
    "Homicide": ["#8b0000"],
    "Burglary": ["#FBBC04"],
    "CriminalDamage": ["#34A853"],
    "Robbery": ["#905922"],
    "SexOffense": ["#000000"],
    "Theft": ["#808000"],
    "VehicleTheft": ["#542f3f"],
    "Arson": ["#ffa500"],
  };

  let legend = document.createElement("div");
  legend.id = "legend";
  legend.style.backgroundColor = "white"; // Add this line to set a background color

  // let titleContainer = document.createElement("div");
  // titleContainer.classList.add("title-container"); // Add this line to set up a container for the title

  // let title = document.createElement("div");
  // title.innerText = "Crime Type";
  // title.classList.add("title");
  // title.style.color = "black"; // Add this line to set text color

  // titleContainer.appendChild(title);
  // legend.appendChild(titleContainer);

  for (let crimeType in colors) {
    let wrapper = document.createElement("div");
    wrapper.classList.add("legend-item"); // Add this line to set up a flex container

    let circle = document.createElement("div");
    circle.style.backgroundColor = colors[crimeType][0];
    circle.style.border = `1px solid ${colors[crimeType][0]}`;
    circle.classList.add("circle"); // Add this line to style the circle

    let txt = document.createElement("div");
    txt.classList.add("legend-text"); // Add this line to style the text
    txt.innerText = crimeType;
    txt.style.color = "black"; // Add this line to set text color

    wrapper.appendChild(circle);
    wrapper.appendChild(txt);
    legend.appendChild(wrapper);
  }

  map.controls[google.maps.ControlPosition.RIGHT_CENTER].push(legend);
}






// Define initMap function
async function initMap() {
  const position = { lat: 43.038902, lng: -87.906471 };
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at the specified position
  map = new Map(document.getElementById("map"), {
    zoom: 15,
    center: position,
    mapId: "65ad242de9b3d35f",
  });

  const datasetId = "889d42e5-3332-4482-9db6-7c8f963c213b";
  const datasetLayer = map.getDatasetFeatureLayer(datasetId);
  datasetLayer.style = setStyle;

  // Call makeLegend after the map is initialized
  makeLegend(map);
}

// Call initMap to initialize the map and create the legend
initMap();
