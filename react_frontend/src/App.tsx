import React, { useEffect, useState } from "react";
import {fetchPartners, fetchTopCountries} from "./api";
import Sidebar from './components/Sidebar';
import WorldMap from './components/WorldMap';
import countryDataJson from "./assets/country_name_to_code.json";
const countryData: Record<string, string> = countryDataJson;

const allCountries = Object.keys(countryData);



function App() {
  // Trading networks state
  const [selectedCountry, setSelectedCountry] = useState<string | null>(null);
  const [partners, setPartners] = useState<string[]>([]);
  const [bottlenecks, setBottlenecks] = useState<{ country: string }[]>([]);
  const [clusters, setClusters] = useState<string[][]>([]);
  const [topCountries, setTopCountries] = useState<
  { code: string, name: string, num_partners: number }[]
  >([]);

  // Control toggles
  const [showPartners, setShowPartners] = useState(true);
  const [showBottlenecks, setShowBottlenecks] = useState(false);
  const [showClusters, setShowClusters] = useState(false);

  useEffect(() => {
    fetchTopCountries(15).then(setTopCountries).catch(console.error);
  }, []);

  // Fetch partners whenever selectedCountry changes
  useEffect(() => {
    if (!selectedCountry) {
      setPartners([]);
      return;
    }
    const selectedCode = selectedCountry ? countryData[selectedCountry] : null;
    if (!selectedCode) {
    setPartners([]);
    console.warn("Country code not found for", selectedCountry);
    return;
    }
    fetchPartners(selectedCode)
      .then(data => setPartners(data.partners || []))
      .catch(() => setPartners([]));
  }, [selectedCountry]);


  // onCountryClick handler
  function handleCountryClick(country: string) {
    setSelectedCountry(country);
  }

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <Sidebar
        countries={allCountries}
        selectedCountry={selectedCountry}
        setSelectedCountry={setSelectedCountry}
        showPartners={showPartners}
        setShowPartners={setShowPartners}
        topCountries={topCountries}
      />
      <div style={{ flex: 1, padding: "2em" }}>
        <h1>Trade Network Analysis</h1>
        <WorldMap
          selectedCountry={selectedCountry}
          partners={showPartners ? partners : []}
          onCountryClick={handleCountryClick}
        />
        {/* Optionally add a CountryInfo component for details */}
        {/* <CountryInfo country={selectedCountry} partners={partners} /> */}
      </div>
    </div>
  );
}

export default App;