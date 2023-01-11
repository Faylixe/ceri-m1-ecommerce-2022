import React, { Component, useState, useRef, useEffect } from "react";
import { Box, Button, Card, CardActionArea, CardContent, CardMedia, Grid, IconButton, Typography } from '@mui/material';
import axios from 'axios';
import { useLocation, useNavigate } from "react-router-dom";
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';


const CartPage = () => {

    const isConnected = true

    const navigate = useNavigate()

    const cart = JSON.parse(localStorage.getItem('cart') || "[]") || [];

    const addToCommand = (item: {}) => {

        const command = JSON.parse(localStorage.getItem('command') || "[]") || [];
        command.push(item)
        localStorage.setItem("command", JSON.stringify(command));
        localStorage.removeItem("cart")
        navigate("/command")
    }

    return (
        <Grid container spacing={2} sx={{ justifyContent: "center", marginTop: "0px", marginBottom: "20px", marginLeft: "calc(80px - 8px)", width: "calc(100% - 160px)" }}>
            <Grid item xs={8} >

                {!isConnected && (<Typography variant="h4" color="text.primary">
                    Connectez-vous pour voir votre panier
                </Typography>)}
                {(cart.length == 0) && (
                    <Typography variant="h4" color="text.primary">
                        Panier vide
                    </Typography>
                )}
                {cart.map((item: any, key: any) => {
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
                                                src={item.image}
                                            />
                                        </Grid>

                                        <Grid item xs={4} >
                                            <Typography variant="h4" color="text.primary">
                                                {item.name}
                                            </Typography>
                                        </Grid>
                                        <Grid item xs={4} sx={{ display: "flex", justifyContent: "space-around" }}>
                                            <Typography variant="h4" color="text.primary">
                                                {item.price} $
                                            </Typography>
                                        </Grid>
                                    </Grid>
                                </CardContent>
                            </CardActionArea>
                        </Card>)
                })}
            </Grid >
            {(cart.length != 0) && (
                <Grid item xs={2}>
                    <Typography variant="h4" color="text.primary">
                        Total du panier :
                    </Typography>

                    <Typography variant="h4" color="text.primary">
                        {cart.reduce((acc: number, a: any) => acc + a.price, 0)} $
                    </Typography>


                    <Button variant="contained" color="primary" sx={{ height: "50px", width: "200px" }}
                        onClick={() => { addToCommand(cart) }}>
                        Commander
                    </Button>
                </Grid>)}
        </Grid >
    )
}

export default CartPage;