# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.define "d.django-forms" do |vm_define|
  end

  config.vm.hostname = "d.django-forms.local"

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 5432, host: 8432

  config.vm.synced_folder "./www", "/home/vagrant/www", create: true

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.name = "d.django-forms"
  end

  config.vm.box_check_update = false
  config.vm.network "private_network", ip: "192.168.33.150"
  config.vm.network "public_network"
end
