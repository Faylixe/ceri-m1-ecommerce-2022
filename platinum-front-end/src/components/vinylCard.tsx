import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { Button, CardActionArea, CardActions } from '@mui/material';

interface vinylCardProps {
    imgPath: string,
    title: string,
    text: string,
    price: string,
    onClick: any
}

const VinylCard = (props: vinylCardProps) => {
    return (
        <Card sx={{ maxWidth: 1080, margin: 2 }} onClick={props.onClick}>
            <CardActionArea>
                <CardMedia
                    component="img"
                    height="140"
                    image={props.imgPath}
                    alt="album cover"
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                        {props.title}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {props.text}
                    </Typography>
                </CardContent>
            </CardActionArea>
        </Card>
    );
}


export default VinylCard;