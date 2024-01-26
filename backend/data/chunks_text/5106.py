- Defines a Stack resource using AWS CDK (Cloud Development Kit).
- Initializes the Stack with required arguments and optional parameters.
- Creates an EC2 VPC (Virtual Private Cloud) with two Availability Zones.
- Creates an ECS Cluster within the VPC.
- Sets up environment variables for the Docker container running Titler.
- Configures gunicorn worker processes based on user input.
- Deploys the application as a Fargate service with Auto Scaling capabilities based on request count and CPU utilization thresholds.
- Allows incoming connections to the load balancer's port 80 from any IP address.