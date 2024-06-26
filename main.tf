resource "kind_cluster" "default" {
    name = "kind-cluster"
    node_image = "kindest/node:v1.30.0"
    kind_config  {
        kind = "Cluster"
        api_version = "kind.x-k8s.io/v1alpha4"
        node {
            role = "control-plane"
        }
        node {
            role =  "worker"
        }
        node {
	    role = "worker"
	}
    }
}
