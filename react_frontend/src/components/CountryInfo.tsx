import React from "react";

// Type for props
interface CountryInfoProps {
  country: string | null;        // Use `null` if that's a possible value; change to `string` if always present
  partners?: string[];           // Optional, may be undefined
}

const CountryInfo: React.FC<CountryInfoProps> = ({ country, partners }) => {
  if (!country) return null;

  return (
    <div className="info">
      <h2>{country}</h2>

      {partners && partners.length > 0 && (
        <>
          <h3>Trading Partners</h3>
          <ul>
            {partners.map(p => (
              <li key={p}>{p}</li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
};

export default CountryInfo;
