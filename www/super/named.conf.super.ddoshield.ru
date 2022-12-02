//
// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
//include "/etc/bind/zones.rfc1918";


# CDN for SNG
view "super.russia" {
    match-clients { AM; AZ; BY; GE; KG; KZ; RU; TM; TJ; UA; UZ; };
    recursion no;

zone "ddoshield.ru" {
        type master;
        file "master/super.ru.ddoshield.ru.zone";
        allow-transfer { 77.222.63.249; };
        allow-update { none; };
};

};



# CDN for Others
view "super.global" {
    match-clients { any; };
    recursion no;

zone "ddoshield.ru" {
        type master;
        file "master/super.de.ddoshield.ru.zone";
        allow-transfer { 77.222.63.249; };
        allow-update { none; };
};



};

