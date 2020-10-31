var redis = require('redis')

var client = redis.createClient(6379,'104.198.244.0');

client.on('connect', function() {
  console.log('connected');
  
});


client.exists('query1', function(err, reply) {

    if (reply === 1) {
        console.log('exists');

	client.get('query1', function(err, reply) {
    		console.log(reply);
	});

    } else {

        console.log('doesn\'t exist');
        client.set('query1', '{"id":1, "name": "adsoft"}')

    }
});
