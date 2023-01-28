import React from "react";
import Navbar from "../components/Navbar";
import { useState } from "react";
import { v4 as uuidv4 } from "uuid";
import Ibex from "../components/49_adobe_express";
import Menu from "../components/menu";
import Timeline from "../components/timeline";

const Home = () => {
  const [itemList, setItemList] = useState("");
  return (
    <div>

      <div className="flex h-screen items-center">
      <div className="bg-ibex-pattern bg-cover bg-center h-screen w-screen fixed">
      <div className="flex h-screen items-center bg-gradient-to-r from-black via-slate-900"></div>

      </div>

        <div className="w-1/12 px-1 border-r">
          <Menu />
        </div>
        <div className="w-11/12 h-screen">
          <div className="relative p-9 text-center">
            <h2 className="justify-center  text-6xl font-bold leading-7 sm:tracking-tight text-white">
              Blue Ibex DAO
            </h2>
          </div>
          <div className="flex flex-row">
            <Timeline />
          </div>
        </div>

      </div>

      
    </div>
  );
};

export default Home;
