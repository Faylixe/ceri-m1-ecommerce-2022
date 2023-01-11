import React, { Component, useState, useRef, useEffect } from "react";
import { Box, Button, Card, CardActionArea, CardContent, CardMedia, Grid, IconButton, Typography } from '@mui/material';
import axios from 'axios';
import { useLocation, useNavigate } from "react-router-dom";
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';


const CommandPage = () => {

    const isConnected = true

    const command = JSON.parse(localStorage.getItem('command') || "[]") || [];

    return (
        <Grid container spacing={2} sx={{ justifyContent: "center", marginTop: "0px", marginBottom: "20px", marginLeft: "calc(80px - 8px)", width: "calc(100% - 160px)" }}>
            <Grid item xs={8} >

                {!isConnected && (<Typography variant="h4" color="text.primary">
                    Connectez-vous pour voir vos commande
                </Typography>)}
                {(command.length == 0) && (
                    <Typography variant="h4" color="text.primary">
                        Pas de commande
                    </Typography>
                )}
                {command.map((item: any, key: any) => {
                    return (
                        <Card variant="outlined">
                            <CardActionArea>
                                <CardContent>
                                    <Grid container spacing={2}>
                                        <Grid item xs={4} >
                                            <Box
                                                component="img"
                                                sx={{
                                                    height: 100,
                                                    width: 100,

                                                }}
                                                alt="cart image"
                                                src={item[0].image}
                                            />
                                        </Grid>
                                        <Grid item xs={4} sx={{ display: "flex", justifyContent: "space-around" }}>
                                            <Typography variant="h4" color="text.primary">
                                                {item.reduce((acc: number, a: any) => acc + a.price, 0)}$
                                            </Typography>
                                        </Grid>
                                    </Grid>
                                </CardContent>
                            </CardActionArea>
                        </Card>)
                })}
            </Grid >
            <Grid item xs={2}>


                {/* <Typography variant="h4" color="text.primary">
                    {cart.reduce((acc: number, a: any) => acc + a.price, 0)} $
                </Typography> */}
            </Grid>
        </Grid >
    )
}

export default CommandPage;