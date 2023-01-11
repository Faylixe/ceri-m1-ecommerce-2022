import React, { Component, useState, useRef, useEffect } from "react";

import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
import VinylCard from "../components/vinylCard";
import { Box, Card, CardActionArea, CardContent, CardMedia, Grid, IconButton, Typography } from '@mui/material';
import ArrowBackIosRoundedIcon from '@mui/icons-material/ArrowBackIosRounded';
import ArrowForwardIosRoundedIcon from '@mui/icons-material/ArrowForwardIosRounded';
import axios from 'axios';
import { useNavigate } from "react-router-dom";


const handleDragStart = (e: { preventDefault: () => any; }) => e.preventDefault();

const responsive = {
    0: { items: 1 },
    1024: { items: 4 },
}

const HomePage = () => {

    const navigate = useNavigate();
    const [items, setItems] = useState<any[]>([]);
    // const items = [
    //     <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    //     <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    //     <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    //     <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    //     <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    //     <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    //     <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"album 1"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} />,
    // ];

    // useEffect(() => {

    //     axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8';
    //     axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    //     axios.get(`https://orangedog-backend-mwjszocsqa-ew.a.run.app/get/albums`, {
    //         headers: {
    //             'Allow-Origin': "*"
    //         }
    //     })
    //         .then((res: { data: any; }) => {

    //             if (res.data) {
    //                 const data = res.data;
    //                 const array: any[] = [];
    //                 data.forEach((element: any) => {
    //                     console.log(element)
    //                     const vinyleCard = <VinylCard imgPath={"https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000"} title={"titre"} text={"le dernier album de artiste 1"} price={"55$"} href={"/album"} onClick={() => {
    //                         navigate("/product", { state: element })
    //                     }} />
    //                     // https://stackoverflow.com/questions/42173786/react-router-pass-data-when-navigating-programmatically
    //                     array.push(vinyleCard)
    //                 });

    //                 setItems(array);
    //             }
    //             else console.log(res)
    //         })
    // });
    const vinyl = [
        {
            id: 1,
            name: "album 1",
            id_artist: 1,
            image: "https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000",
            type: "rock",
            price: 55.0,
            songs: []
        },
        {
            id: 2,
            name: "album 2",
            id_artist: 1,
            image: "https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000",
            type: "rock",
            price: 55.0,
            songs: []
        },
        {
            id: 3,
            name: "album 3",
            id_artist: 1,
            image: "https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000",
            type: "rock",
            price: 55.0,
            songs: []
        },
        {
            id: 4,
            name: "album 4",
            id_artist: 1,
            image: "https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000",
            type: "rock",
            price: 55.0,
            songs: []
        },
        {
            id: 5,
            name: "album 5",
            id_artist: 1,
            image: "https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000",
            type: "rock",
            price: 55.0,
            songs: []
        },
        {
            id: 6,
            name: "album 6",
            id_artist: 1,
            image: "https://img.freepik.com/free-psd/vinyl-record-cover-with-orange-background-mockup_23-2149379034.jpg?w=2000",
            type: "rock",
            price: 55.0,
            songs: []
        }
    ]
    useEffect(() => {

        const array: any[] = [];
        vinyl.forEach((element: any) => {
            console.log(element)
            const vinyleCard = <VinylCard imgPath={element.image} title={element.name} text={"le dernier album de artiste 1"} price={element.price} onClick={() => {
                navigate("/product", { state: element })
            }} />
            // https://stackoverflow.com/questions/42173786/react-router-pass-data-when-navigating-programmatically
            array.push(vinyleCard)
        });

        setItems(array);

    });

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