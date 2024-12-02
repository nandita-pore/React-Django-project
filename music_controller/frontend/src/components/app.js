import React from "react";
import {render} from "react-dom";
import { HomePage } from "./HomePage";
import { RoomJoinPage } from "./RoomJoinPage";
import { CreateRoomPage } from "./CreateRoomPage";

export const App =()=>{
    return(
        <div>

        <HomePage/>
        <RoomJoinPage/>
        <CreateRoomPage/>
        </div>
    )
}



const appDiv = document.getElementById("app");
render(<App/>,appDiv);