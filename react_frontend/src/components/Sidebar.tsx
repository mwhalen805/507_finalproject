import React from "react";

// Adjust `string[]` if your countries are richer objects, e.g., { code: string, name: string }
interface TopCountry {
  code: string;
  name: string;
  num_partners: number;
}

interface SidebarProps {
  countries: string[];
  selectedCountry: string | null;
  setSelectedCountry: (country: string) => void;
  showPartners: boolean;
  setShowPartners: (value: boolean) => void;
  topCountries: TopCountry[]
}

const Sidebar: React.FC<SidebarProps> = ({
  countries,
  selectedCountry,
  setSelectedCountry,
  showPartners,
  setShowPartners,
  topCountries
}) => {
  return (
    <div className="sidebar">
      <h2>Controls</h2>

      <label>
        <input
          type="checkbox"
          checked={showPartners}
          onChange={() => setShowPartners(!showPartners)}
        />
        Show Trading Partners
      </label>

      <h3>Select a country</h3>
      <select
        value={selectedCountry || ""}
        onChange={e => setSelectedCountry(e.target.value)}
      >
        <option value="">-- Choose --</option>
        {countries.map(c => (
          <option key={c} value={c}>{c}</option>
        ))}
      </select>
      <h3>Top Trading Countries</h3>
      <ol>
        {topCountries.map(tc => (
          <li key={tc.code}>
            <button
              style={{ background: "none", border: "none", padding: 0, cursor: "pointer", color: "#1565c0" }}
              onClick={() => setSelectedCountry(tc.name)}
            >
              {tc.name}
            </button>
            {" "}
            ({tc.num_partners})
          </li>
        ))}
      </ol>
    </div>
  );
};

export default Sidebar;