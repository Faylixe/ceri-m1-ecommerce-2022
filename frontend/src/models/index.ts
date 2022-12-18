import type {
  IAlbum,
  IArtist,
  ICartItem,
  ICategory,
  IOrderDetail,
  IOrderItem,
  IPaymentDetail,
  IPromo,
  IShoppingSession,
  ISong,
  IUser,
  IUserAddress,
} from "@/interfaces/index";

export class Song implements ISong {
  id?: number;
  title!: string;
  release_date!: string;
  cover!: string;
  album_id!: number;

  constructor(fields?: Partial<ISong>) {
    Object.assign(this, fields);
  }
}

export class Album implements IAlbum {
  id?: number;
  title!: string;
  release_date!: string;
  cover?: string = "default url";
  artist_id!: number;
  price!: number;
  stock_qty!: number;
  description!: string;
  category_id!: number;
  list_song?: ISong[] = [];

  constructor(fields?: Partial<IAlbum>) {
    Object.assign(this, fields);
  }

  set_list_song(songs: Song[]) {
    this.list_song = songs.filter((songs) => songs.album_id == this.id);
  }
}

export class Artist implements IArtist {
  id?: number = -1;
  firstname: string = "";
  lastname: string = "";
  date_of_birth?: string = Date();
  cover?: string = "url";
  list_album?: Album[] = [];

  constructor(fields?: Partial<IArtist>) {
    Object.assign(this, fields);
  }

  set_list_album(albums: Album[]) {
    this.list_album = albums.filter((album) => album.id == this.id);
  }
}

export class Promo implements IPromo {
  id?: number = -1;
  start_date!: string;
  end_date!: string;
  rate!: number;
  album_id!: number;

  constructor(fields?: Partial<IPromo>) {
    Object.assign(this, fields);
  }
}

export class Category implements ICategory {
  id?: number = -1;
  label!: string;
  list_album?: Album[] = [];
  constructor(data: Partial<ICategory>) {
    Object.assign(this, data);
  }
  set_list_album(albums: Album[]) {
    this.list_album = albums.filter((album) => album.id == this.id);
  }
}


export class OrderDetail implements IOrderDetail {
  id?: number;
  total: number = 0;
  user_id: number = 0;
  payment_status: boolean = false;
  delivery_status: boolean = false;
  orders_status: string = "";
  created_date?: string;
  list_payment: PaymentDetail[] = [];
  created_date?: Date | undefined;
  constructor(fields: Partial<IOrderDetail>) {
    Object.assign(this, fields);
  }
 
}
export class OrderItem implements IOrderItem {
  id?: number;
  qty = 0;
  order_detail_id = 0;
  album_id = 0;
  created_date?: Date;
  constructor(fields: Partial<IOrderItem>) {
    Object.assign(this, fields);
  }
}
export class PaymentDetail implements IPaymentDetail {
  id?: number;
  name?: string;
  card_number?: string;
  provider?: string;
  expiration_date?: string;
  status = "";
  created_date?: string;
  constructor(fields: Partial<IOrderItem>) {
    Object.assign(this, fields);
  }
}

export class ShoppingSession implements IShoppingSession {
  id?: number;
  total = 0;
  user_id = 0;
  created_date?: Date;
  constructor(fields: Partial<IShoppingSession>) {
    Object.assign(this, fields);
  }
}

export class User implements IUser {
  id?: number;
  username = "";
  firstname?: string;
  telephone?: string;
  email?: string;
  password?: string;
  created_date?: Date;
  is_admin: boolean = false;
  list_address: UserAddress[] = [];
  list_shopping_session: ShoppingSession[] = [];
  list_order_detail: OrderDetail[] = [];
  constructor(fields: Partial<IUser>) {
    Object.assign(this, fields);
  }
}
export class UserAddress implements IUserAddress {
  id?: number;
  adress_line1 = "";
  adress_line2?: string;
  city = "";
  country = "";
  postal_code = "";
  mobile?: string;
  user_id = 0;
  created_date?: Date;
  constructor(fields: Partial<IUserAddress>) {
    Object.assign(this, fields);
  }
}
