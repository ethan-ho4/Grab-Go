// import React, { useEffect, useState, useMemo } from "react";
// import {GoogleMap, useLoadScript, Marker} from "@react-google-maps/api";

// export default function LatLon() {
//     const [lat, setLat] = useState()
//     const [lon, setLon] = useState()

//     useEffect(()=>{
//         navigator.geolocation.getCurrentPosition((position)=>{
//             setLat(position.coords.latitude)
//             setLon(position.coords.longitude)
//         })
//     })
    
//     const { isLoaded } = useLoadScript({
//         googleMapsApiKey: process.env.NEXT_PUBLIC_GOOGLE_MAPS_API_KEY,
//       });
    
//     if (!isLoaded) return <div>.Loading...</div>;
//     return <Map />


// function Map() {
//     const center = useMemo(() =>({lat: lat, lon: lon}), []);
  
//     return (
//       <GoogleMap zoom = {10} center = {center} mapContainerClassName = "map-container">
//         <Marker position = {center} />
//       </GoogleMap>
//     );
// }}