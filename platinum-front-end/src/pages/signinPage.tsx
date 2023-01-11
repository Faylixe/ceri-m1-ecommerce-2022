import React, { Component, useState, useRef, useEffect, useContext } from "react";
import { Box, Button, Card, CardActionArea, CardContent, CardMedia, Grid, IconButton, TextField, Typography } from '@mui/material';
import axios from 'axios';
import { useLocation, useNavigate } from "react-router-dom";
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import { AppContext } from "../App";


const SigninPage = () => {

    const navigate = useNavigate()
    const appContextValue = useContext(AppContext)
    const isConnected = appContextValue?.isConnected
    const setUser = appContextValue?.setUser
    const setIsConnected = appContextValue?.setIsConnected

    // if (isConnected) {
    //     navigate("/")
    // }

    const [username, setUserName] = useState('');
    const [password, setPassword] = useState('');

    const [isError, setIsError] = useState(false)

    const checkUser = () => {
        if (username === "ok") {
            setIsError(false)

            if (setUser && setIsConnected) {
                setUser({ id: "salut" })
                setIsConnected(true)
                console.log("réussi")
                navigate(-1)
            }

        }
        else {
            setIsError(true)
            console.log("reffusé")
        }
    }

    return (
        <Grid container spacing={2} sx={{ justifyContent: "center", marginTop: "0px", marginBottom: "20px", marginLeft: "calc(80px - 8px)", width: "calc(100% - 160px)" }}>
            <Grid item xs={8} >


                <Card variant="outlined">
                    <CardActionArea>
                        <CardContent sx={{ display: "flex", justifyContent: "space-around", flexDirection: "column" }}>
                            <Typography variant="h4" color="text.primary">
                                Connexion
                            </Typography>
                            <Typography variant="h5" color="text.primary">
                                Username
                            </Typography>
                            <TextField
                                required
                                error={isError}
                                id="outlined-required"
                                label="username"
                                onChange={e => setUserName(e.target.value)}
                            />
                            <Typography variant="h5" color="text.primary">
                                Password
                            </Typography>
                            <TextField
                                required
                                error={isError}
                                id="outlined-password-input"
                                label="Password"
                                type="password"
                                autoComplete="current-password"
                                onChange={e => setPassword(e.target.value)}
                            />
                            {/* <input type="password" onChange={e => setPassword(e.target.value)} /> */}
                            <Button variant="contained" color="primary" sx={{ height: "50px", width: "200px" }}
                                onClick={checkUser}>
                                Connexion
                            </Button>
                        </CardContent>
                    </CardActionArea>
                </Card>
            </Grid >
        </Grid >
    )
}

export default SigninPage;