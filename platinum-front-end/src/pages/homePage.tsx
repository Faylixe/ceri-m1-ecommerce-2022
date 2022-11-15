import React, { Component, useState, useRef } from "react";

import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
import VinylCard from "../components/vinylCard";
import { Box, Card, CardActionArea, CardContent, CardMedia, Grid, IconButton, Typography } from '@mui/material';
import ArrowBackIosRoundedIcon from '@mui/icons-material/ArrowBackIosRounded';
import ArrowForwardIosRoundedIcon from '@mui/icons-material/ArrowForwardIosRounded';


const handleDragStart = (e: { preventDefault: () => any; }) => e.preventDefault();

const items = [
    <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
];

const responsive = {
    0: { items: 1 },
    1024: { items: 4 },
}

const HomePage = () => {

    const RenderNextButton = () => {
        return (
            <IconButton style={{ position: "absolute", right: 0, top: "100px" }}>
                <ArrowForwardIosRoundedIcon />
            </IconButton>
        )
    };

    const RenderPrevButton = () => {
        return (
            <IconButton style={{ position: "absolute", left: 0, top: "100px" }}>
                <ArrowBackIosRoundedIcon />
            </IconButton>
        )
    };

    return (
        <>
            <Typography
                variant="h6"
                sx={{ marginLeft: "40px", marginTop: "20px" }}
                onClick={() => {
                    alert('You clicked the title!')
                }}
            >
                Top des ventes
            </Typography>
            <AliceCarousel
                responsive={responsive}
                mouseTracking
                disableDotsControls
                items={items}
                paddingLeft={20}
                paddingRight={20}
                keyboardNavigation={true}
                renderPrevButton={() => {
                    return <RenderPrevButton />
                }}
                renderNextButton={() => {
                    return <RenderNextButton />
                }}
            />
            <Typography
                variant="h6"
                sx={{ marginLeft: "40px", marginTop: "-10px" }}
                onClick={() => {
                    alert('You clicked the title!')
                }}
            >
                Catégories les plus apréciés
            </Typography>
            <Grid container spacing={2} sx={{ marginTop: "0px", marginBottom: "20px", marginLeft: "calc(80px - 8px)", width: "calc(100% - 160px)" }}>
                <Grid item xs={6}>
                    <Card>
                        <CardActionArea>
                            <CardMedia
                                component="img"
                                height="140"
                                image=""
                                alt="album cover"
                            />
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="div">
                                    titre
                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    texte
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>
                </Grid>
                <Grid item xs={6}>
                    <Card>
                        <CardActionArea>
                            <CardMedia
                                component="img"
                                height="140"
                                image=""
                                alt="album cover"
                            />
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="div">
                                    titre
                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    texte
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>
                </Grid>
                <Grid item xs={4}>
                    <Card>
                        <CardActionArea>
                            <CardMedia
                                component="img"
                                height="140"
                                image=""
                                alt="album cover"
                            />
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="div">
                                    titre
                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    texte
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>
                </Grid>
                <Grid item xs={4}>
                    <Card>
                        <CardActionArea>
                            <CardMedia
                                component="img"
                                height="140"
                                image=""
                                alt="album cover"
                            />
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="div">
                                    titre
                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    texte
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>
                </Grid>
                <Grid item xs={4}>
                    <Card>
                        <CardActionArea>
                            <CardMedia
                                component="img"
                                height="140"
                                image=""
                                alt="album cover"
                            />
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="div">
                                    titre
                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    texte
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>
                </Grid>
            </Grid>


        </>
    )

}

export default HomePage;