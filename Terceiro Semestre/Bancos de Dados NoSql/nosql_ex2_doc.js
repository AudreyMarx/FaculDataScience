db.postagem.insert([

    { titulo: 'Banco de dados orientado a documentos',
    detalhes: 'é um dos modelos de bancos de dados NOSQL',    
    autor: 'curso NOSQL', 
    link_site: 'www.curso_de_nosql.com',    
    tags: ['banco de dados', 'NOSQL', 'MongoDB'],    
    nr_de_likes: 1000},
    
    { titulo: 'NoSQL Database',    
    detalhes: "CouchDb usa views ao invés de coleções",    
    autor: 'curso NOSQL',    
    link_site: 'www.curso_de_nosql.com',    
    tags: ['banco de dados', 'NOSQL', 'CouchDB'],    
    nr_de_likes: 200,    
    comentario:[{login:'usuario1',mensagem:'post1',data:new Date("2020-08-30"),like:0}]}])