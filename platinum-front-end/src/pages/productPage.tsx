import React, { Component, useState, useRef, useEffect } from "react";
import { Box, Button, Card, CardActionArea, CardContent, CardMedia, Grid, IconButton, Typography } from '@mui/material';
import axios from 'axios';
import { useLocation, useNavigate } from "react-router-dom";
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';


const ProductPage = () => {

    const { state } = useLocation()

    const product = state

    console.log(state)

    const isConnected = true

    return (
        <Grid container spacing={2} sx={{ justifyContent: "center", marginTop: "0px", marginBottom: "20px", marginLeft: "calc(80px - 8px)", width: "calc(100% - 160px)" }}>
            <Grid item xs={8} >

                {!isConnected && (<Typography variant="h4" color="text.primary">
                    Connectez-vous pour pouvoir ajouter au panier
                </Typography>)}
                <Card variant="outlined">
                    <CardActionArea>
                        <CardMedia
                            component="img"
                            image={product.image}
                            alt="album cover"
                            sx={{ width: "200px", height: "200px" }}
                        />
                        <CardContent>
                            <Grid container spacing={2}>
                                <Grid item xs={8} >
                                    <Typography variant="h4" color="text.primary">
                                        {product.name}
                                    </Typography>
                                    <Typography variant="h5" color="text.secondary">
                                        Description
                                    </Typography>
                                    <Typography variant="h6" color="text.secondary">
                                        blablabla de produit
                                    </Typography>
                                </Grid>
                                <Grid item xs={4} sx={{ display: "flex", justifyContent: "space-around" }}>
                                    <Typography variant="h4" color="text.primary">
                                        {product.price} $
                                    </Typography>
                                    <Button variant="contained" disabled={!isConnected} color="primary" sx={{ height: "50px", width: "50px" }}>
                                        <AddShoppingCartIcon />
                                    </Button>
                                </Grid>
                            </Grid>
                        </CardContent>
                    </CardActionArea>
                </Card>
            </Grid >
        </Grid >
    )
}

export default ProductPage;