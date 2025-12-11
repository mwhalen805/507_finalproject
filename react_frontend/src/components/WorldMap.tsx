import React from "react";
import {
  ComposableMap,
  Geographies,
  Geography
} from "react-simple-maps";
import countryDataJson from "../assets/country_name_to_code.json";
const nameToCode: Record<string, string> = countryDataJson;

const geoUrl =
  "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json";

interface WorldMapProps {
  selectedCountry: string | null;
  partners: string[];
  onCountryClick: (country: string) => void;
}

const WorldMap: React.FC<WorldMapProps> = ({
  selectedCountry,
  partners,
  onCountryClick
}) => {
  // Prepare fast lookup sets
  const partnerSet = new Set(partners || []);


  // Distinct color palette for clusters (feel free to customize/make longer!)
  const clusterColors = ["#fde047", "#fca5a5", "#a5f3fc", "#34d399", "#a78bfa"];

  return (
    <ComposableMap projection="geoMercator" width={900} height={500}>
      <Geographies geography={geoUrl}>
        {({ geographies }: { geographies: any[] }) =>
          geographies.map((geo: any) => {
            // For world-atlas topojson, names are under geo.properties.name
            const countryName: string = geo.properties.name;
            const countryCode: string | undefined = nameToCode[countryName];
            if (!countryCode) {
              return <Geography key={geo.rsmKey} geography={geo} style={{ default: { outline: "none", fill: "#EEE" } }} />;
            }

            let fill = "#EEE"; // default grey

            if (selectedCountry === countryName) {
              fill = "#4f46e5"; // blue for selected
            } else if (partnerSet.has(countryCode)) {
              fill = "#22c55e"; // green for trading partners
            }

            return (
              <Geography
                key={geo.rsmKey}
                geography={geo}
                onClick={() => onCountryClick(countryName)}
                style={{
                  default: { outline: "none", fill },
                  hover: { outline: "none", fill: "#94a3b8" },
                  pressed: { outline: "none" }
                }}
              />
            );
          })
        }
      </Geographies>
    </ComposableMap>
  );
};

export default WorldMap;